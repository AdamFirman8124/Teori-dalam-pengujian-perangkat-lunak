

# Generated at 2022-06-13 22:01:55.176959
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    f = JSONFormatter()
    assert (f.format_body(
        "{ \"a\": 12, \"b\": true, \"c\": null, \"d\": [  1, 2, 3 ], \"e\": { \"f\": \"g\" } }",
        'json'
    ) == "{\n    \"a\": 12,\n    \"b\": true,\n    \"c\": null,\n    \"d\": [\n        1,\n        2,\n        3\n    ],\n    \"e\": {\n        \"f\": \"g\"\n    }\n}")

# Generated at 2022-06-13 22:02:05.491821
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # test with json request
    jsonFormatter = JSONFormatter(explicit_json=True)
    request = '{"test": "hello", "test2": "thanks"}'
    response = '{"test2": "thanks", "test": "hello"}'
    assert jsonFormatter.format_body(request, 'application/json') == response
    # test with no json
    jsonFormatter = JSONFormatter(explicit_json=False)
    request = '{"test": "hello", "test2": "thanks"}'
    response = '{"test": "hello", "test2": "thanks"}'
    assert jsonFormatter.format_body(request, 'text/plain') == response

# Generated at 2022-06-13 22:02:12.922938
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    f = JSONFormatter()
    assert(f.format_body('{ "b": "c" }', 'json') == '{\n    "b": "c"\n}')
    assert(f.format_body('{ "b": "c" }', 'text') == '{\n    "b": "c"\n}')
    assert(f.format_body('{ "b": "c" }', 'html') == '{ "b": "c" }')

# Generated at 2022-06-13 22:02:22.514016
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():

    json_formatter = JSONFormatter(format_options={
        'json': {
            'format': True,
            'indent': 4,
            'sort_keys': True
        }
    },
        explicit_json=True,
        output_options={'style': 'colors'})
    assert json_formatter.enabled is True
    assert json_formatter.kwargs['explicit_json'] is True
    assert json_formatter.format_options['json']['sort_keys'] is True
    assert json_formatter.format_options['json']['indent'] == 4
    assert json_formatter.kwargs['output_options']['style'] == 'colors'


# Generated at 2022-06-13 22:02:34.463104
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.context import Environment
    from pygments.formatters import TerminalTrueColorFormatter # type: ignore
    from pygments.lexers import JsonLexer # type: ignore
    import json
    # setup
    formatter = JSONFormatter(
        environment=Environment(),
        format_options={
            'colors': True,
            'style': TerminalTrueColorFormatter,
            'json': {
                'format': True,
                'indent': 2,
                'sort_keys': True
            }
        },
        lexer=JsonLexer(),
        is_terminal=True,
        should_strip_colors=False,
        explicit_json=False,
        stdout_isatty=True,
        style_error=TerminalTrueColorFormatter().style_error
    )
    # list


# Generated at 2022-06-13 22:02:45.145363
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    import io
    import json
    import sys

    # simulate parameters
    params = {}
    params['explicit_json'] = True
    params['format_options'] = {}
    params['format_options']['json'] = {}
    params['format_options']['json']['indent'] = None
    params['format_options']['json']['sort_keys'] = False
    params['format_options']['json']['format'] = True

    # simulate I/O
    sysin = sys.stdin
    sysout = sys.stdout
    sys.stdin = io.StringIO('{"name": "Kevin", "age": 25}')
    sys.stdout = io.StringIO()

    # execute tested method
    formatter = JSONFormatter(**params)
    formatter.format_

# Generated at 2022-06-13 22:02:49.937683
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    formatter = JSONFormatter()
    formatter.get_content_type() == 'application/json'
    assert formatter.get_content_type() == 'application/json'
    assert formatter.format() == '{}'
    assert json.loads(formatter.format()) == {}

# Generated at 2022-06-13 22:02:57.639539
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()
    input = '{"key1": "value1", "key2": "value2", "key3": {"key4": "value4"}}'
    assert formatter.format_body(input, 'json') == '{\n    "key1": "value1",\n    "key2": "value2",\n    "key3": {\n        "key4": "value4"\n    }\n}'
    assert formatter.format_body(input, 'application/json') == '{\n    "key1": "value1",\n    "key2": "value2",\n    "key3": {\n        "key4": "value4"\n    }\n}'

# Generated at 2022-06-13 22:03:08.321953
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Test for json formatted
    json_formatter_1 = JSONFormatter(
        format_options={
            'json': {'format': True, 'indent': 4, 'sort_keys': True}},
        explicit_json=True
    )
    raw_json = '{\n' \
               '  "a": "b",\n' \
               '  "c": "d"\n' \
               '}'
    formated_json = json_formatter_1.format_body(raw_json, 'json')
    assert_that(formated_json).is_equal_to(raw_json)

    # Test for no json formatted

# Generated at 2022-06-13 22:03:09.999697
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    JSONFormatter(pretty=True)


# Generated at 2022-06-13 22:03:27.017782
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter()
    assert json_formatter.format_body('{"foo": "bar"}', 'json') == '{\n    "foo": "bar"\n}'
    assert json_formatter.format_body('{"foo": "bar"}', 'javascript') == '{\n    "foo": "bar"\n}'
    assert json_formatter.format_body('{"foo": "bar"}', 'text') == '{\n    "foo": "bar"\n}'
    assert json_formatter.format_body('{"foo": "bar"}', 'application/json') == '{\n    "foo": "bar"\n}'
    assert json_formatter.format_body('{"foo": "bar"}', 'application/javascript') == '{\n    "foo": "bar"\n}'

# Generated at 2022-06-13 22:03:29.763309
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    new_json_formatter = JSONFormatter(json={'format': True, 'indent': 4, 'sort_keys': True})

# Generated at 2022-06-13 22:03:37.018434
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    """Verify body is correctly processed."""
    json_formatter = JSONFormatter(explicit_json=False)

    body = '{"a": "b"}'
    response_mimetype = 'application/json'
    assert json_formatter.format_body(body) == '{\n    "a": "b"\n}'

    body = '{"a": "b"}'
    response_mimetype = 'application/not-json'
    assert json_formatter.format_body(body) == body

# Generated at 2022-06-13 22:03:38.989163
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    new_JSONFormatter = JSONFormatter()
    assert new_JSONFormatter

# Generated at 2022-06-13 22:03:46.499663
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    jf = JSONFormatter(explicit_json=True, format_options={'json':{'format':True, 'indent':4, 'sort_keys':False}})
    assert jf.kwargs['explicit_json']
    assert jf.enabled
    assert jf.format_options['json']['format']
    assert jf.format_options['json']['indent'] == 4
    assert not jf.format_options['json']['sort_keys']


# Generated at 2022-06-13 22:03:52.565626
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
  # Test constructor with no key-value arguments
  json_formatter = JSONFormatter()
  assert(json_formatter.enabled == False)

  # Test constructor with keyword-value arguments
  json_formatter = JSONFormatter(format_options = {'json': {'format': True, 'indent': 2, 'sort_keys': False}})
  assert(json_formatter.enabled == True)

# Generated at 2022-06-13 22:04:02.414033
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from tests.data import valid_json_content, valid_json_content_with_indent_and_sorted_keys
    import json
    import httpie
    assert JSONFormatter(
        format_options = {
            'json': {
                'format': True,
                'indent': 4,
                'sort_keys': True
            }
        },
        explicit_json=False,
        zero_or_one=None,
        output_options=dict()
    ).format_body(valid_json_content, 'application/json') == json.dumps(
        obj=json.loads(valid_json_content),
        sort_keys=True,
        ensure_ascii=False,
        indent=4
    )

# Generated at 2022-06-13 22:04:12.599204
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter(format_options={'json' : {'format': True, 'sort_keys': True, 'indent': 2}})
    body = json_formatter.format_body('{"uid": "test", "children": ["test1", "test2"]}', 'application/json')
    assert body == '{\n  "children": [\n    "test1",\n    "test2"\n  ],\n  "uid": "test"\n}'
    body = json_formatter.format_body('{"uid": "test", "children": ["test1", "test2"]}', 'text/json')

# Generated at 2022-06-13 22:04:26.298074
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    formatter = JSONFormatter()
    assert formatter.kwargs == {}
    assert formatter.format_options == {'json': {'format': True, 'indent': 4, 'sort_keys': False}}
    assert formatter.enabled == True
    kwargs = {'verbose': True}
    formatter = JSONFormatter(**kwargs)
    assert formatter.kwargs == kwargs
    assert formatter.format_options == {'json': {'format': True, 'indent': 4, 'sort_keys': False}}
    assert formatter.enabled == True
    format_options = {'json': {'format': False, 'indent': 2, 'sort_keys': True}}
    formatter = JSONFormatter(format_options=format_options, **kwargs)

# Generated at 2022-06-13 22:04:33.257467
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(format_options=None, kwargs=None)
    assert formatter.format_body('{"b": [1, 2], "a": 1}', 'json') == '{\n    "a": 1,\n    "b": [\n        1,\n        2\n    ]\n}'

# Generated at 2022-06-13 22:04:55.165413
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    #Routine to test format_body of class JSONFormatter
    json_formatter = JSONFormatter()
    json_formatter.kwargs = {'explicit_json': False}
    json_formatter.format_options = {
            'json': {
                'format': True,
                'indent': None,
                'sort_keys': False,
                'compress': False,
            }
    }
    maybe_json = [
        'json',
        'javascript',
        'text',
    ]
    body = r'{'
    mime = 'a'
    assert json_formatter.format_body(body, mime) == body
    body = r'{'
    mime = 'json'
    assert json_formatter.format_body(body, mime) == body

# Generated at 2022-06-13 22:04:59.436324
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.formatters import JSONFormatter

    body = '{"key":"value"}'
    expected = '{\n    "key": "value"\n}'

    formatter = JSONFormatter(indent=4, sort_keys=True)
    result = formatter.format_body(body, 'json')

    assert expected == result

# Generated at 2022-06-13 22:05:07.060350
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Create a test object of class JSONFormatter
    json_formatter = JSONFormatter()
    # Test method format_body with test arguments
    assert json_formatter.format_body(body='', mime='') == ''
    assert json_formatter.format_body(body='{}', mime='') == '{\n}\n'
    assert json_formatter.format_body(body='""', mime='') == '""'
    assert json_formatter.format_body(body='a', mime='') == 'a'
    assert json_formatter.format_body(body='{test:test}', mime='') == '{test:test}'
    # Test method format_body with invalid JSON string

# Generated at 2022-06-13 22:05:13.237752
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    foo = JSONFormatter(
        session=None,
        format_options={
            'headers':{},
            'json':{
                'format':True,
                'indent':4,
                'sort_keys':False
                },
            'pretty':{
                'format':True,
                'all':False,
                'colors':True,
                'flow_style':False
            },
            'colors':True,
            'stream':True,
            'style':True,
            'verify':True,
            },
        explicit_json=False,
        stdin=True,
        stdin_isatty=False
    )
    assert foo.format_options['json']['format']
    assert foo.format_options['json']['indent'] == 4
    assert foo.format_options

# Generated at 2022-06-13 22:05:20.650792
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    jsonFormatter = JSONFormatter()
    assert jsonFormatter.format_body('{"k1": 42, "k2": "v2"}', 'application/json') == '{\n    "k1": 42,\n    "k2": "v2"\n}'
    assert jsonFormatter.format_body('{"k1": 42, "k2": "v2"}', 'text/plain') == '{\n    "k1": 42,\n    "k2": "v2"\n}'
    assert jsonFormatter.format_body('{"k1": 42, "k2": "v2"}', 'text/html') == '{\n    "k1": 42,\n    "k2": "v2"\n}'

# Generated at 2022-06-13 22:05:31.255418
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    print('test_JSONFormatter_format_body')

    from httpie.core import main

    f = main.get_formatter(None, None,
        explicit_json=True,
        json={
            'format': True,
            'indent': 4,
            'sort_keys': True
        }
    )

    assert isinstance(f, JSONFormatter)
    assert f.format_options == {
        'json': {
            'format': True,
            'indent': 4,
            'sort_keys': True
        }
    }

    from httpie.core import main

    # json == {'foo': 'bar'}

# Generated at 2022-06-13 22:05:38.625714
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    from httpie.context import Environment
    from httpie.config import Config
    from httpie.plugins import BuiltinPluginManager
    env = Environment(Config(), BuiltinPluginManager())
    formatter = JSONFormatter(env)
    assert formatter.kwargs['explicit_json'] == False
    assert formatter.kwargs['style'] == env.style
    assert formatter.kwargs['format_options'] == env.config.format_options
    assert formatter.enabled == False


# Generated at 2022-06-13 22:05:47.730174
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    import httpie
    from httpie.plugins import JSONFormatter, FormatterPlugin
    JSONFormatter.kwargs = {
        'explicit_json': False,
        'formatted': False,
        'format_options': {
            'json': {
                'format': True,
                'indent': 2,
                'sort_keys': False}}
    }
    FormatterPlugin.kwargs = JSONFormatter.kwargs
    result = JSONFormatter.format_body('{"test": "test"}', 'json')
    assert result == '{\n  "test": "test"\n}'

# Generated at 2022-06-13 22:05:55.998437
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # return body as is when mime is not json
    formatter_plugin = JSONFormatter(explicit_json=False,
                                     format_options={'json': {'format': True,
                                                              'indent': 2}})
    body = '{"hello":"world"}'
    expected_formatted_body = '{"hello":"world"}'
    assert formatter_plugin.format_body(body, 'text/html') == expected_formatted_body
    assert formatter_plugin.format_body(body, 'text/json') == expected_formatted_body
    assert formatter_plugin.format_body(body, 'text/javascript') == expected_formatted_body
    assert formatter_plugin.format_body(body, 'text/x-javascript') == expected_formatted_body

# Generated at 2022-06-13 22:06:06.304457
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    JSONFormatter_plugin = JSONFormatter(format_options={'json': {'format':True, 'indent':4, 'sort_keys':True}})
    actual1 = JSONFormatter_plugin.format_body(body='{"a": 1, "b": 2}', mime='application/json')
    expected1 = '{\n    "a": 1,\n    "b": 2\n}'
    assert actual1 == expected1
    actual2 = JSONFormatter_plugin.format_body(body='{"a": 1, "b": 2}', mime='text')
    expected2 = '{\n    "a": 1,\n    "b": 2\n}'
    assert actual2 == expected2

# Generated at 2022-06-13 22:06:38.999416
# Unit test for method format_body of class JSONFormatter

# Generated at 2022-06-13 22:06:46.874020
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # JSONFormatter.format_body returns the json string indented, ordered and with ascii encoding
    # Input data
    body = '[{"key1":"value1","key2":2},{"key1":"value1","key2":2}]'
    formatter = JSONFormatter(format_options={'json' : {'format':True, 'indent':2, 'sort_keys':True}})
    output = formatter.format_body(body, 'text/json')
    assert output == '[\n  {\n    "key1": "value1",\n    "key2": 2\n  },\n  {\n    "key1": "value1",\n    "key2": 2\n  }\n]'

# Generated at 2022-06-13 22:07:01.756620
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()

    # No JSON content
    test_string = 'x01x'
    expected_result = test_string
    formatted_body = formatter.format_body(test_string,'text')
    assert(formatted_body == expected_result)

    # Valid JSON content
    test_string = '{"message" : "Hello World"}'
    expected_result = test_string
    formatted_body = formatter.format_body(test_string,'text')
    assert(formatted_body == expected_result)

    # Invalid JSON content
    test_string = '{"message" : "Hello World]!'
    expected_result = test_string
    formatted_body = formatter.format_body(test_string,'text')
    assert(formatted_body == expected_result)

# Generated at 2022-06-13 22:07:03.072020
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()


# Generated at 2022-06-13 22:07:10.713155
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    from httpie.plugins import FormatterPlugin

    fp = FormatterPlugin(format_options={
        'json': {
            'format': True,
            'indent': 2,
            'sort_keys': True
        }
    })
    assert fp.kwargs == {'explicit_json': False}
    assert fp.format_options['json']['format'] == True
    assert fp.format_options['json']['indent'] == 2
    assert fp.format_options['json']['sort_keys'] == True


# Unit test to test format_body function of class JSONFormatter

# Generated at 2022-06-13 22:07:16.065765
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    formatter = JSONFormatter(kwargs={'explicit_json': True,
                                      'format_options': {'json': {'format': True}}})
    assert formatter.kwargs['explicit_json'] is True
    assert formatter.format_options['json']['format'] is True

# Generated at 2022-06-13 22:07:18.023373
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    try:
        JSONFormatter()
    except:
        assert False



# Generated at 2022-06-13 22:07:26.648100
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    import io
    from httpie.output.streams import BINARY_SUPPRESSED_NOTICE
    from tests.compat import mock

    formatter = JSONFormatter()

    fake_stdout = io.BytesIO()
    formatter.kwargs = {
        'explicit_json': True,
        'output_options': {
            'verify': True,
            'verify_ssl': True
        },
        'stdin': None,
        'stdin_isatty': False,
        'stdout': fake_stdout,
        'stdout_isatty': True
    }

    # 'text/plain'
    assert formatter.format_body('{"a": 1}', 'text/plain') == '{"a": 1}'

    # 'application/json'
    assert formatter.format_

# Generated at 2022-06-13 22:07:35.658617
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from base64 import b64encode
    from datetime import datetime
    import httpie.output.formatters.json
    import tests.output
    import tests.data
    import tests.plugins

    # https://docs.python.org/3.6/library/datetime.html#datetime-objects
    now = datetime.now()
    now_base64 = b64encode(now.isoformat().encode())

    # https://jsonapi.org/
    json_api_base64 = b64encode(
        json.dumps(
            obj={
                "jsonapi": {
                    "version": "1.0"
                },
            }
        ).encode()
    )

    # https://facebook.github.io/graphql/

# Generated at 2022-06-13 22:07:45.739933
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():

    # # Test case 1: no json content in body
    jsonFormatter = JSONFormatter()
    body = "# Not JSON content"
    mime = 'text'
    out = jsonFormatter.format_body(body, mime)
    assert out == body

    # # Test case 2: input is not JSON content
    jsonFormatter = JSONFormatter()
    body = "Not JSON content"
    mime = 'text'
    out = jsonFormatter.format_body(body, mime)
    assert out == body

    # # Test case 3: no json content in body, but explicit_json enabled
    jsonFormatter = JSONFormatter()
    jsonFormatter.kwargs['explicit_json'] = True
    body = "# Not JSON content"
    mime = 'text'

# Generated at 2022-06-13 22:08:06.247856
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
   import httpie
   from httpie.core import main
   from httpie.output.streams import BINARY_SUPPRESSED_NOTICE

   output_data = main([
      '--output-format=json',
      '--output-options=sort_keys=True,indent=4',
      '--verbose',
      'GET',
      'https://httpbin.org/get'
   ])

# Generated at 2022-06-13 22:08:19.201675
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(
        sort_keys=True,
        indent=None,
        explicit_json=False
    )

    # Test with valid json
    assert formatter.format_body('{"a": "b"}', 'json') == '{"a":"b"}'
    assert formatter.format_body('{"a": "b"}', 'text') == '{"a":"b"}'
    assert formatter.format_body('{"a": "b"}', 'javascript') == '{"a":"b"}'

    # Test with invalid json
    assert formatter.format_body('{"a": "b}', 'json') == '{"a": "b}'
    assert formatter.format_body('{"a": "b}', 'text') == '{"a": "b}'

# Generated at 2022-06-13 22:08:25.669670
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(format_options={"json": {"format": True, "indent": 2, "sort_keys": True}})
    assert formatter.format_body("{\"baz\": [1, 2, 3], \"foo\": 1, \"bar\": 2}", "json") == "{\n  \"bar\": 2,\n  \"baz\": [\n    1,\n    2,\n    3\n  ],\n  \"foo\": 1\n}"
    assert formatter.format_body("{\"baz\": [1, 2, 3], \"foo\": 1, \"bar\": 2}", "javascript") == "{\n  \"bar\": 2,\n  \"baz\": [\n    1,\n    2,\n    3\n  ],\n  \"foo\": 1\n}"


# Generated at 2022-06-13 22:08:36.050527
# Unit test for method format_body of class JSONFormatter

# Generated at 2022-06-13 22:08:44.721575
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter(sort_keys=False, indent=2)

# Generated at 2022-06-13 22:08:51.517826
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    obj = {
        'a': 1,
        'b': 2,
        'c': [
            3,
            4,
            5,
            6,
        ]
    }

    off = json.dumps(obj=obj, sort_keys=False, indent=None)
    on = json.dumps(obj=obj, sort_keys=True, indent=2)

    t = JSONFormatter(explicit_json=False,
                      format_options={'json': {'format': True, 'sort_keys': True, 'indent': 2}}).format_body(
        body=off, mime='json')
    assert t == on

# Generated at 2022-06-13 22:08:58.378078
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()
    # body is not json,
    # mime is not in maybe_json
    assert formatter.format_body('hello', 'html') == 'hello'
    # body is not json,
    # mime is in maybe_json
    assert formatter.format_body('hello', 'text') == 'hello'
    # body is json
    assert formatter.format_body('{"hello": "world"}', 'json') == '{\n  "hello": "world"\n}'

# Generated at 2022-06-13 22:09:08.751255
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(**{'format_options': {'json': {'format': True, 'indent': 4, 'sort_keys': True, 'flow_style': False}}})
    body = '[{"haha": "heihei", "id": 1, "name": "dupeng"}, {"haha": "heihei", "id": 2, "name": "dupeng"}]'
    mime = 'json'
    assert formatter.format_body(body, mime) == '[\n   {\n      "haha": "heihei",\n      "id": 1,\n      "name": "dupeng"\n   },\n   {\n      "haha": "heihei",\n      "id": 2,\n      "name": "dupeng"\n   }\n]'

# Generated at 2022-06-13 22:09:15.561222
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    body = '{"result": 1}'  # Valid JSON
    mime = 'application/json'  # One of mayType
    fmt = JSONFormatter(kwargs={'explicit_json': False}, format_options={'json':{'format': False, 'sort_keys':False,'indent':0}})
    res = fmt.format_body(body, mime)
    assert res == body  # Check that result was correct
    body = '{"result": 1}'  # Valid JSON
    mime = 'not-json'  # not mayType
    fmt = JSONFormatter(kwargs={'explicit_json': False}, format_options={'json':{'format': False, 'sort_keys':False,'indent':0}})
    res = fmt.format_body(body, mime)
    assert res == body

# Generated at 2022-06-13 22:09:23.996485
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Test format_body for content-type 'application/json'.
    jf = JSONFormatter(explicit_json=False,
                       format_options={
                            'json': {
                                'format': True,
                                'indent': '  ',
                                'sort_keys': False
                            }})
    body = '{"a":1,"b":2}'
    assert body == jf.format_body(body, 'application/json')

    # Test format_body for content-type 'application/json; charset=UTF-8'.
    jf = JSONFormatter(explicit_json=False,
                       format_options={
                            'json': {
                                'format': True,
                                'indent': '  ',
                                'sort_keys': False
                            }})

# Generated at 2022-06-13 22:09:52.626899
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    body = """{"value": 2, "key": "test"}"""
    mime = "application/json"
    formatted_body = JSONFormatter().format_body(body, mime)
    prettied_body = """{
  "key": "test",
  "value": 2
}"""
    assert formatted_body == prettied_body

# Generated at 2022-06-13 22:10:04.808641
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter()
    assert json_formatter.format_body('{ "a": 1 }', 'javascript') == '{\n    "a": 1\n}'
    assert json_formatter.format_body('{ "a": 1 }', 'xml') == '{ "a": 1 }'
    assert json_formatter.format_body('{ "a": 1 }', 'json') == '{\n    "a": 1\n}'
    assert json_formatter.format_body('{ "a": 1 }', 'text') == '{\n    "a": 1\n}'
    assert json_formatter.format_body('{ "a": 1 }', 'html') == '{ "a": 1 }'

# Generated at 2022-06-13 22:10:14.884562
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    assert JSONFormatter().format_body('{"foo":"bar"}', 'application/json') == '{\n    "foo": "bar"\n}\n'
    assert JSONFormatter().format_body("{'foo':'bar'}", 'application/json') == "{'foo':'bar'}"
    assert JSONFormatter().format_body("{'foo':'bar'}", 'application/javascript') == "{'foo':'bar'}"
    assert JSONFormatter().format_body("{'foo':'bar'}", 'application/beautiful') == "{'foo':'bar'}"
    assert JSONFormatter().format_body("{'foo':'bar'}", 'application/javascrip') == "{'foo':'bar'}"

# Generated at 2022-06-13 22:10:19.804134
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    format_options = {'json':
                      {'format': True,
                       'indent': 4,
                       'sort_keys': True}
                      }

    json_formatter = JSONFormatter(format_options=format_options,
                                   explicit_json=True)

    # Check valid JSON.
    result = json_formatter.format_body('{"a": "b"}', 'application/json')
    expected = '{\n    "a": "b"\n}'
    assert result == expected

    # Check invalid JSON.
    result = json_formatter.format_body('{"a": "b"', 'application/json')
    expected = '{"a": "b"'
    assert result == expected

    # Check non-JSON with json mime type.

# Generated at 2022-06-13 22:10:34.366392
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    jf = JSONFormatter(format_options={'json': {'format': True, 'indent': 2, 'sort_keys': True}})
    out = jf.format_body(body='{"key": "value"}', mime='application/json')
    assert out == '{\n  "key": "value"\n}'

    jf = JSONFormatter(format_options={'json': {'format': True, 'indent': 0, 'sort_keys': True}})
    out = jf.format_body(body='{"key": "value"}', mime='application/json')
    assert out == '{"key": "value"}'

    jf = JSONFormatter(format_options={'json': {'format': False, 'indent': 0, 'sort_keys': True}})
    out = jf

# Generated at 2022-06-13 22:10:41.680672
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter()
    result = json_formatter.format_body(body='{"b": 1, "a": {"b": 1, "a": 0}}', mime='json')
    assert result == '{\n    "a": {\n        "a": 0,\n        "b": 1\n    },\n    "b": 1\n}'
    result = json_formatter.format_body(body='{"b": 1, "a": {"b": 1, "a": 0}}', mime='text')
    assert result == '{\n    "a": {\n        "a": 0,\n        "b": 1\n    },\n    "b": 1\n}'
    result = json_formatter.format_body(body='{"b": "a"}', mime='text')

# Generated at 2022-06-13 22:10:53.201630
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Test function format_body of class JSONFormatter
    # Create a instance of class JSONFormatter
    json_formatter = JSONFormatter(format_options={
        'json': {'format': True, 'indent': 4, 'sort_keys': True}},
        options={})

    # Normal test
    assert json_formatter.format_body(
        body='{"a":1,"b":2,"c":3,"d":4}',
        mime='json') == '{\n    "a": 1,\n    "b": 2,\n    "c": 3,\n    "d": 4\n}'

    # The body is not JSON type, so return original body

# Generated at 2022-06-13 22:10:59.608417
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Test with valid JSON
    HTTPIE_ARGS = [
        ('--json',),
        ('--json', '--json-sort-keys'),
        ('--json', '--json-indent',),
        ('--json', '--json-sort-keys', '--json-indent'),
    ]
    for httpie_arg in HTTPIE_ARGS:
        f = JSONFormatter(_kwargs=dict(vars(FormatterPlugin.parse_options(httpie_arg))))
        assert f.format_body('{"a":1,"b":2}',
                             'application/json') == '{\n  "a": 1,\n  "b": 2\n}'

#    # Test with invalid JSON
#    with pytest.raises(ValueError):
#        f.format_body('{"a:

# Generated at 2022-06-13 22:11:02.424161
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    import httpie.plugins.json
    assert isinstance(httpie.plugins.json.JSONFormatter, object)



# Generated at 2022-06-13 22:11:09.737957
# Unit test for method format_body of class JSONFormatter