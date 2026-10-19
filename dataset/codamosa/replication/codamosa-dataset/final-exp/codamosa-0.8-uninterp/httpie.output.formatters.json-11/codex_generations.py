

# Generated at 2022-06-13 22:01:47.662247
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    args = {}
    JSONFormatter(**args)

# Generated at 2022-06-13 22:01:49.977370
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    json_formatter = JSONFormatter()
    assert json_formatter.enabled == None


# Generated at 2022-06-13 22:01:53.099775
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    # arrange
    sut = JSONFormatter  # system under test
    # act
    # assert

# Generated at 2022-06-13 22:01:58.875635
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    assert JSONFormatter().format_body("{}", "json") == "{}"
    assert JSONFormatter().format_body("{}", "text") == "{}"
    assert JSONFormatter().format_body("{}", "javascript") == "{}"
    assert JSONFormatter().format_body("{}", "php") != "{}"

# Generated at 2022-06-13 22:02:09.217457
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.plugins import FormatterPlugin

    class JSONFormatter(FormatterPlugin):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.enabled = 'all'
        def format_body(self, body: str, mime: str) -> str:
            return body
    assert JSONFormatter(explicit_json=False, format_options={
        'json': {
            'sort_keys': False,
            'indent': 3,
            'format': True
        }
    }).format_body('{"a": 1, "b": 2}', 'application/json') == '''{
   "a": 1,
   "b": 2
}'''

# Generated at 2022-06-13 22:02:21.204383
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.plugins import FormatterPluginManager
    from httpie.context import Environment
    env = Environment()
    plugin_manager = FormatterPluginManager()
    plugin_manager.register(JSONFormatter)
    env.formatter = plugin_manager.get(env, 'JSONFormatter')
    # Test case when json field of format_options is enabled
    env.formatter.enabled = True
    assert env.formatter.format_body('{"a": 1, "b": 2}', 'json') == '{\n    "a": 1,\n    "b": 2\n}'
    # Test case when json field of format_options is disabled
    env.formatter.enabled = False

# Generated at 2022-06-13 22:02:25.760949
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()
    assert formatter.format_body('{"a": 2, "d": 3, "b": "hello"}', "json") == '{\n  "a": 2,\n  "b": "hello",\n  "d": 3\n}'

# Generated at 2022-06-13 22:02:29.974223
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    jf = JSONFormatter(options={'json':{'format': True, 'indent':1, 'sort_keys': False}}, explicit_json=False)
    assert jf.enabled

# Generated at 2022-06-13 22:02:39.489486
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter()
    # Unit test for method format_body of class JSONFormatter
    # when the body is well-formed json
    assert json_formatter.format_body('{"hello": "world", "spam": "eggs"}', 'json') == '{\n    "hello": "world",\n    "spam": "eggs"\n}'
    assert json_formatter.format_body('{"hello": "world", "spam": "eggs"}', 'javascript') == '{\n    "hello": "world",\n    "spam": "eggs"\n}'

# Generated at 2022-06-13 22:02:49.817698
# Unit test for method format_body of class JSONFormatter

# Generated at 2022-06-13 22:03:07.444433
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    jf = JSONFormatter()
    # Test 1
    body = "{\n    \"one\": 1,\n    \"two\": 2,\n    \"three\": 3\n}"
    mime = 'application/json'
    actual = jf.format_body(body, mime)
    expected = body
    assert actual == expected
    # Test 2
    body = "{\n    \"one\": 1,\n    \"two\": 2,\n    \"three\": 3\n}"
    mime = 'text/html'
    actual = jf.format_body(body, mime)
    expected = body
    assert actual == expected
    # Test 3
    body = "{'one': 1, 'two': 2, 'three': 3}"
    mime = 'application/json'
    actual = jf.format_body

# Generated at 2022-06-13 22:03:16.562903
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    body1 = '{"key1": "value1", "key2": "value2"}'
    mime1 = 'application/json'
    body2 = '[1, 2, 3, 4]'
    mime2 = 'application/json'
    body3 = '{"key1": "value1", "key2": "value2"}'
    mime3 = 'application/javascript'
    body4 = '<h1>Hello, world</h1>'
    mime4 = 'text/html'
    body5 = '{"key1": "value1", "key2": "value2"}'
    mime5 = 'text/json'
    body6 = '{"key1": "value1", "key2": "value2"}'
    mime6 = 'text/javascript'

    json_formatter = JSONFormatter

# Generated at 2022-06-13 22:03:21.804097
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    body = '[{"key": "param1", "value": "value1"}]'
    mime = 'application/json'
    formatter = JSONFormatter()
    body = formatter.format_body(body, mime)
    assert body == '[\n    {\n        "key": "param1",\n        "value": "value1"\n    }\n]'


# Generated at 2022-06-13 22:03:23.019878
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    assert JSONFormatter is not None

# Generated at 2022-06-13 22:03:36.059357
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.plugins import JSONFormatter
    from httpie.compat import OrderedDict
    from json.decoder import JSONDecodeError

    test_input = OrderedDict([("a", 3), ("b", 2), ("c", 1)])
    test_input2 = OrderedDict([("b", 5), ("c", 4), ("d", 3)])

    test_input_json = json.dumps(test_input, indent=2, sort_keys=True)
    test_input2_json = json.dumps(test_input2, indent=2, sort_keys=True)

    test_output = json.dumps(test_input, indent=4, sort_keys=True)


# Generated at 2022-06-13 22:03:45.017529
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    assert JSONFormatter(
                format_options={
                    'json': {
                        'format': True,
                        'sort_keys': False,
                        'indent': 2
                    }
                }
            ).format_body('{}', 'json') == '{\n  \n}'
    assert JSONFormatter(
                format_options={
                    'json': {
                        'format': True,
                        'sort_keys': True,
                        'indent': 0
                    }
                }
            ).format_body(
                '{"b":2,"a":1}',
                'json'
            ) == '{"a":1,"b":2}'

# Generated at 2022-06-13 22:03:53.216506
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.plugins.builtin import JSONFormatter as JSONFormatter_builtin
    from httpie.plugins import JSONFormatter
    fmtr = JSONFormatter(explicit_json=False)
    fmtr_builtin = JSONFormatter_builtin(explicit_json=False)
    assert fmtr.format_body("{\n  \"id\": 1\n}", 'application/json') == \
        fmtr_builtin.format_body("{\n  \"id\": 1\n}", 'application/json')

# Generated at 2022-06-13 22:03:59.767703
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    fmt = JSONFormatter()
    assert fmt.format_body('{}', 'json') == '{}'
    assert fmt.format_body('{"a": 1, "b": 2}', 'json') == '{\n    "a": 1,\n    "b": 2\n}'
    assert fmt.format_body('{"a": 1, "b": 2}', 'text/html') == '{"a": 1, "b": 2}'

# Generated at 2022-06-13 22:04:12.512892
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    f = JSONFormatter()
    assert f.format_body({"a": 1}, 'application/json') == '{"a": 1}'
    assert f.format_body('{"a": 1}', 'application/json') == '{"a": 1}'
    assert f.format_body('a', 'application/json') == '"a"'
    assert f.format_body({"a": 1}, 'text/plain') == '{"a": 1}'
    assert f.format_body('{"a": 1}', 'text/plain') == '{"a": 1}'
    assert f.format_body('a', 'text/plain') == '"a"'



# Generated at 2022-06-13 22:04:20.948864
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    json_formatter = JSONFormatter(format_options={
        'json': {
            'format': True,
            'indent': 2,
            'sort_keys': True,
        },
        'headers': {
            'format': True,
            'colors': False,
            'completer': True,
        },
        'status': {
            'format': True,
            'colors': False,
        },
        'body': {
            'format': True,
            'colors': False,
            'completer': True,
            'style_output': False,
            'style_errors': True,
            'style_overrides': [],
        },
    }, kwargs={
        'explicit_json': False,
        'style': None
    })
    assert json_formatter

# Generated at 2022-06-13 22:04:39.750041
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    assert JSONFormatter().format_body(
        '{"a": "1"}', 'application/json') == '{\n    "a": "1"\n}'
    assert JSONFormatter().format_body(
        '{"a": "1"}', 'application/json; charset=utf-8') == '{\n    "a": "1"\n}'
    assert JSONFormatter().format_body(
        '{"a": "1"}', 'json') == '{\n    "a": "1"\n}'
    assert JSONFormatter().format_body(
        '{"a": "1"}', 'text/json') == '{\n    "a": "1"\n}'

# Generated at 2022-06-13 22:04:46.522573
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_fmt = JSONFormatter()
    json_fmt.kwargs = {'explicit_json': False}

    body = '{"bar": "baz", "qux": ["corge", "grault"], "waldo": "fred"}'
    formatted = json.loads(json_fmt.format_body(body, 'text'))
    expected = json.loads(body)

    assert formatted == expected
    assert json_fmt.format_body(body, 'json') == body

# Generated at 2022-06-13 22:04:59.314448
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(
        format_options = {
            'json': {
                'format': True,
                'indent': None,
                'sort_keys': False
            }
        }
    )
    result = formatter.format_body("{'a': 1, 'b': 2}", 'json')
    assert result == "{'a': 1, 'b': 2}"
    result = formatter.format_body("{'a': 1, 'b': 2}", 'text')
    assert result == "{'a': 1, 'b': 2}"
    result = formatter.format_body("{'a': 1, 'b': 2}", 'javascript')
    assert result == "{'a': 1, 'b': 2}"
    formatter.format_options['json']['indent'] = 2
   

# Generated at 2022-06-13 22:05:07.006397
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.core import main
    from tests.data import (
        BIN_FILE_PATH,
        FILE_PATH_ARG,
        FILE_PATH,
        JSON_FILE_PATH,
        JSON_FILE_CONTENT,
        JSON_FILE_OBJECT,
        BIN_FILE_CONTENT,
        BIN_FILE_ARG,
    )
    from pytest import raises
    from httpie.compat import str

    # Enable json format.
    main.HTTPie([])._format_options['json']['format'] = True

    # Test json content
    out = main.HTTPie([]).run(
        ['-v', '-b', '-f', JSON_FILE_PATH])
    assert 0 == out.exit_status
    assert out.json == JSON_FILE_OBJECT

   

# Generated at 2022-06-13 22:05:09.951175
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    assert JSONFormatter().format_body('{"foo":"bar"}', 'application/json') == '{\n    "foo": "bar"\n}'

# Generated at 2022-06-13 22:05:25.764249
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # construct
    formatter = JSONFormatter(format_options={
        'json': {
            'format': True,
            'sort_keys': False,
            'indent': None,
        },
        'colors': {
            'request_method': 'red',
            'request_url': 'white',
            'request_http_version': 'green',
        },
    }, explicit_json=True)
    # test
    result = formatter.format_body(body='{"hello":"world"}', mime='json')
    assert result == '{\n    "hello": "world"\n}'
    formatter.enabled = False
    result = formatter.format_body(body='{"hello":"world"}', mime='json')
    assert result == '{"hello":"world"}'

# Generated at 2022-06-13 22:05:35.551683
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    jsonFormatter = JSONFormatter(
        explicit_json=True,
        format_options={
            'json': {
                'format': True,
                'indent': 2,
                'sort_keys': True
            }
        }
    )
    body_dict = {
        "method": "get",
        "headers": {
            "Content-Encoding": "gzip",
            "User-Agent": "test agent"
        },
        "content": {
            "username": "test",
            "password": "test"
        }
    }
    body = json.dumps(body_dict, indent=2, sort_keys=True, ensure_ascii=False)
    assert body == jsonFormatter.format_body(json.dumps(body_dict), "json")
    assert json.dumps

# Generated at 2022-06-13 22:05:42.771397
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()
    assert formatter.format_body("{'foo': 1, 'bar': 2}", 'json') == '{\n    "foo": 1,\n    "bar": 2\n}'
    assert formatter.format_body("{'foo': 1, 'bar': 2}", 'javascript') == '{\n    "foo": 1,\n    "bar": 2\n}'
    assert formatter.format_body("{'foo': 1, 'bar': 2}", 'text') == '{\n    "foo": 1,\n    "bar": 2\n}'
    assert formatter.format_body("{'foo': 1, 'bar': 2}", 'something else') == "{'foo': 1, 'bar': 2}"

# Generated at 2022-06-13 22:05:47.909464
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Setup
    formatter = JSONFormatter()
    body = '{"a": "b"}'
    mime = 'json'
    # Exercise
    response = formatter.format_body(body, mime)
    # Assert
    assert response == '{\n  "a": "b"\n}'


# Generated at 2022-06-13 22:05:49.860579
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    assert JSONFormatter.__name__ == 'JSONFormatter'
    assert JSONFormatter.__doc__ == 'json formatter'

# Generated at 2022-06-13 22:06:14.166585
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from unittest.mock import Mock

    kwargs = {
        'format_options': {
            'json': {
                'format': True,
                'indent': 2,
                'sort_keys': True,
            },
        },
        'explicit_json': False,
    }
    instance = JSONFormatter(**kwargs)

    body = '{"a": 1, "b": 2}'
    mime = 'json'
    assert instance.format_body(body, mime) == '{\n  "a": 1,\n  "b": 2\n}'

    body = '{"a": 1, "b": 2}'
    mime = 'javascript'

# Generated at 2022-06-13 22:06:22.919279
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    obj_test = [{"test_key1": "test_value1", "test_key2": "test_value2"}]
    body_test = json.dumps(obj=obj_test, ensure_ascii=True, sort_keys=True, indent=4)
    assert JSONFormatter(explicit_json=True,
                         format_options={'json': {'format': True, 'sort_keys': True, 'indent': 4}}
                         ).format_body(body=body_test, mime='json') == body_test

# Generated at 2022-06-13 22:06:28.153783
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_format = JSONFormatter()

    formating_body = '{"id":"236","name":"John Doe","age":"25"}'
    json_format.format_body(formating_body, 'json') == formating_body

# Generated at 2022-06-13 22:06:38.314860
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    """
    Test that the format_body method returns a string that is parsable as JSON
    (without including the brackets inevitably introduced by httpbin)
    Test that the format_body method doesn't transform a string that is not parsable as JSON
    """
    f = JSONFormatter()
    
    json_string = '{"key1": "value1", "key2": "value2"}'
    not_json_string = '{"key1": "value1" "key2": "value2"}'
    
    assert json.loads(f.format_body(json_string, 'json'))
    assert json.loads(f.format_body('[{},{}]'.format(json_string, json_string), 'json'))
    
    assert f.format_body(not_json_string, 'json') == not_json_

# Generated at 2022-06-13 22:06:47.411343
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from collections import OrderedDict
    from httpie.plugins import FormatterPlugin
    json_formatter = JSONFormatter(
        format_options={'json': {'format': True, 'sort_keys': True, 'indent': 2}},
        explicit_json=False,
        colors=False
    )
    assert json_formatter.format_body(
        '{"a": 1, "b": 2, "c": 3}',
        'application/json'
    ) == '{\n  "a": 1,\n  "b": 2,\n  "c": 3\n}'

# Generated at 2022-06-13 22:06:55.418433
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Create test object
    formatter = JSONFormatter(
        format_options={
            'json': {
                'format': True,
                'indent': 2,
                'sort_keys': True
            }
        },
        kwargs={
            'explicit_json': True
        }
    )
    # Test case 1
    body = '{"a": 1, "b": 2}'
    mime = 'application/json'
    assert formatter.format_body(body, mime) == '{\n  "a": 1,\n  "b": 2\n}'
    # Test case 2
    body = '{"a": 1, "b": 2}'
    mime = 'application/x-javascript'

# Generated at 2022-06-13 22:07:02.292288
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.utils import TestEnvironment
    from httpie.context import Environment
    from httpie.plugins.builtin import JSONFormatter

    formatter = JSONFormatter()

    env = TestEnvironment()
    env.stdout = None
    formatter = JSONFormatter()
    formatter.env = env

    data = '{"foo":42, "bar" : "http://example.com/baz"}'

    # unmodified
    assert formatter.format_body(data, mime='text/html') == data

    # no formatting
    assert formatter.format_body(data, mime='application/json') == data

    # modified
    assert '  ' in formatter.format_body(data, mime='application/json', explicit_json=True)

# Generated at 2022-06-13 22:07:11.651783
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.cli import mockargs
    from httpie.context import Environment
    from httpie.plugins import FormatterPlugin
    import json

    # Test a wrong JSON
    format_options = {
        'json': {
            'format':True,
            'indent':2,
            'sort_keys':True
        }
    }
    kwargs = {'explicit_json':True}
    body = '{"status":"ok"}3.14'
    mime = 'json'
    assert JSONFormatter(
        format_options=format_options,
        kwargs=kwargs
    ).format_body(body=body, mime=mime) == body, 'The JSON is not valid and should not be formatted'

    # Test a valid JSON

# Generated at 2022-06-13 22:07:15.140130
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter()
    body = '{ "a": "b" }'
    mime = 'json'
    result = json_formatter.format_body(body, mime)

    expected_result = '{\n    "a": "b"\n}'
    assert result == expected_result

# Generated at 2022-06-13 22:07:16.775739
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    json_formatter = JSONFormatter()
