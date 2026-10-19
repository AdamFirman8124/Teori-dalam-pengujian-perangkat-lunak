

# Generated at 2022-06-13 22:01:53.239955
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    expected_body = json.dumps(
        obj={'key': 'value', 'user': {'name': 'Jane Doe', 'age': '20', 'email': 'janedoe@email.com'}},
        sort_keys=False,
        ensure_ascii=False,
        indent=4
    )
    jsonFormatter = JSONFormatter()
    assert(jsonFormatter.format_body('{"key": "value", "user": {"name": "Jane Doe", "age": "20", "email": "janedoe@email.com"}}', 'json') == expected_body)
    

# Generated at 2022-06-13 22:01:57.860877
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    import tempfile

    json_formatter = JSONFormatter(format_options={'json': {'format': True,
                                                             'sort_keys': True,
                                                             'indent': 2,
                                                             'explicit_json': True}})
    assert json_formatter.enabled is True

# Generated at 2022-06-13 22:02:03.936763
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    try:
        obj = JSONFormatter(
            format_options={
                "json": {
                    'format': "formater",
                    'sort_keys': "sort_keys",
                    'indent': "indent"
                }
            },
            explicit_json="explicit_json"
        )
    except Exception:
        assert False

# Generated at 2022-06-13 22:02:11.910682
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    import httpie.input
    import httpie.cli
    import httpie.output

    args = httpie.cli.parser.parse_args([
        '--json',
    ])
    args.output_options = httpie.output.parse_options(args)
    args.output_options.prettify = True
    args.output_options.formatted = True
    json_formatter = httpie.output.JSONFormatter(args)

    body = '{"key1":"value1", "key2":"value2"}'
    mimetype = 'application/json'
    assert json_formatter.format_body(body, mimetype) == \
        json_formatter.format_body(body, mimetype)

    body = '{"key2":"value2","key1":"value1"}'

# Generated at 2022-06-13 22:02:22.629277
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():

    json_formatter = JSONFormatter()
    json_formatter.format_options = {
        'json': {
            'format': True,
            'sort_keys': True,
            'indent': 4
        }
    }

    body = '{"a": 1, "b": 2}'
    assert json_formatter.format_body(body=body,
                                      mime='json') == '{\n    "a": 1,\n    "b": 2\n}'

    body = '{"a": 1, "b": 2}'
    assert json_formatter.format_body(body=body,
                                      mime='application/json') == '{\n    "a": 1,\n    "b": 2\n}'

    body = '{"a": 1, "b": 2}'
   

# Generated at 2022-06-13 22:02:34.463574
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(
        format_options={ 'json':{
                            'format': 1,
                            'indent': 4,
                            'sort_keys': 0,
                            'explicit_json': 0,
                            }},
    )
    mime = 'json'

# Generated at 2022-06-13 22:02:45.145805
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter(format_options='{"json": {"format": true}}')
    maybe_json = [
        'json',
        'javascript',
        'text',
    ]
    assert json_formatter.format_body('{"a": "b"}', "json") == '{\n    "a": "b"\n}'
    assert json_formatter.format_body('{"a": "b"}', "javascript") == '{\n    "a": "b"\n}'
    assert json_formatter.format_body('{"a": "b"}', "text") == '{\n    "a": "b"\n}'
    assert json_formatter.format_body('{"a": "b"}', "") == '{"a": "b"}'
    assert json_formatter.format_

# Generated at 2022-06-13 22:02:55.103550
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    kwargs = {'explicit_json': False}
    format_options = {'json': {'format': True, 'sort_keys': True, 'indent': 4}}
    formatter = JSONFormatter(kwargs=kwargs, format_options=format_options)
    body_in = '{"foo": "bar", "baz": "qux"}'
    mime = 'json'
    body_out = formatter.format_body(body_in, mime)
    expected_out = '{\n    "baz": "qux",\n    "foo": "bar"\n}'
    assert body_out == expected_out


# Create a JSONFormatter object and import it into the global scope as
# `formatter`.
formatter = JSONFormatter

# Generated at 2022-06-13 22:03:02.851815
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    body = '{"a": 1}'
    mime = 'json'
    formatter = JSONFormatter()
    formatter.kwargs['explicit_json'] = False
    formatter.format_options['json']['indent'] = 4
    formatter.format_options['json']['sort_keys'] = True
    formatted_body = formatter.format_body(body, mime)
    assert formatted_body == '{\n    "a": 1\n}'

# Generated at 2022-06-13 22:03:12.430106
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(format_options=None, explicit_json=False, style=None)
    body = '{"foo": "bar"}'
    mime = 'application/json'
    assert formatter.format_body(body, mime) == '{\n    "foo": "bar"\n}'
    mime = 'application/javascript'
    assert formatter.format_body(body, mime) == '{\n    "foo": "bar"\n}'
    mime = 'text/javascript'
    assert formatter.format_body(body, mime) == '{\n    "foo": "bar"\n}'
    mime = 'text/plain'
    assert formatter.format_body(body, mime) == '{\n    "foo": "bar"\n}'
    #

# Generated at 2022-06-13 22:03:29.042307
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.plugins import FormatterPlugin, PluginManager
    from httpie.formatter import format_options
    pm = PluginManager(format_options)
    plugin = JSONFormatter(format_options)
    plugin.enabled = True

    # When json is explicitly enabled
    # body is converted to json
    body, mime = '{"foo": "bar"}', 'json'
    assert plugin.format_body(body, mime) == '{\n    "foo": "bar"\n}'

    # When json is not explicitly enabled,
    # don't convert body to json
    body, mime = '{"foo": "bar"}', 'html'
    assert plugin.format_body(body, mime) == '{"foo": "bar"}'

    # When invalid JSON is passed
    # don't convert body to json
    body,

# Generated at 2022-06-13 22:03:33.942523
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    formatter = JSONFormatter({'json': {'format': True, 'indent': 2, 'sort_keys': True}})
    assert formatter.format_options['json']['indent'] == 2


# Generated at 2022-06-13 22:03:36.861127
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    body = JSONFormatter(None, None).format_body('{"key": "value"}', 'application/json')
    assert body == '{\n    "key": "value"\n}'

# Generated at 2022-06-13 22:03:52.022978
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    assert JSONFormatter().enabled == False
    assert JSONFormatter(explicit_json=True).enabled == True
    assert JSONFormatter(
        format_options={
            'json': {
                'format': True,
                'indent': 4,
                'sort_keys': True,
            },
        }
    ).enabled == True
    assert JSONFormatter(
        format_options={
            'json': {
                'format': True,
                'indent': 4,
                'sort_keys': True,
            },
        },
        explicit_json=False
    ).enabled == True

# Generated at 2022-06-13 22:04:02.601640
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # test case 1
    body = '123'
    mime = 'json'
    assert JSONFormatter().format_body(body, mime) == '123'
    # test case 2
    body = '{"a": 1, "b": 2, "c": 3}'
    mime = 'json'
    assert JSONFormatter().format_body(body, mime) == '{\n    "a": 1,\n    "b": 2,\n    "c": 3\n}'
    # test case 3
    body = '{"a": 1, "b": 2, "c": 3}'
    mime = 'text'

# Generated at 2022-06-13 22:04:12.471411
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.core import main

    from .test_utils import bin_json_data

    # Run httpie and capture output
    args = [
        '--json',
        '--print', 'HB',
    ]
    env = {}
    r = main(args, env=env)
    out, err = r.stderr_bytes, r.stderr
    out = out.decode()

    # Note: The output of httpie is in bytes. Here we decode it to a string
    #       so that it can be used in the assert statement.

    # Test the output with binary data
    assert bin_json_data.decode() in out
    # Test the output with JSON data
    assert '{"field1":"value1","field2":"value2"}' in out

# Generated at 2022-06-13 22:04:20.918147
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    assert JSONFormatter().format_body('{}', 'json') == '{}'
    assert JSONFormatter().format_body('{"a": 47}', 'json') == '{\n    "a": 47\n}'
    assert JSONFormatter().format_body('{"a": 47}', 'javascript') == '{\n    "a": 47\n}'
    assert JSONFormatter().format_body('{"a": 47}', 'text') == '{\n    "a": 47\n}'
    assert JSONFormatter().format_body('{"a": 47}', 'foo') == '{"a": 47}'
    assert JSONFormatter(format_options={'json': {'format': True}}).format_body('{}', 'json') == '{}'

# Generated at 2022-06-13 22:04:35.653473
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    import inspect

    import httpie.cli.argtypes as argtypes
    from httpie.context import Environment

    from test_api import simple_json, simple_json_str, complex_json, complex_json_str

    # Use the capture_kwargs decorator to inspect the kwargs
    # of the decorated function, in this case method JSONFormatter.format_body
    # itself.
    @argtypes.capture_kwargs(argtypes.JSON)
    def env_init(**kwargs):
        env = Environment()
        env.formats['json'] = {}
        env.formats['json'].update(kwargs)
        return env

    def format_body(*args, env=None, **kwargs):
        if env is None:
            return None

# Generated at 2022-06-13 22:04:42.044759
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    instance = JSONFormatter(
        format_options={
            'json': {
                'format': True,
                'indent': 2,
                'sort_keys': False,
            }
        })

    body = "{{'name':'Vinh', 'age': 20, 'location': 'Hanoi'}}"
    mime = 'json'
    output = instance.format_body(body=body, mime=mime)

    assert isinstance(output, str)

# Generated at 2022-06-13 22:04:53.723008
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Using a JSONFormatter with default values:
    #   - json is enabled;
    #   - json.format is True;
    #   - json.sort_keys is False;
    #   - json.indent is 2,
    #   - --json is False.
    formatter = JSONFormatter(format_options={'json': {'format':True, 'sort_keys':False, 'indent':2}}, kwargs={'explicit_json':False})

    # Format a JSON as if it hasn't been formatted before.
    json_str = '{"json": ["formatted"]}'
    assert formatter.format_body(json_str, "application/json") == '{\n  "json": [\n    "formatted"\n  ]\n}'

    # Format a formatted JSON.
    formatted

# Generated at 2022-06-13 22:05:01.465402
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    f = JSONFormatter()
    assert f.enabled
    assert f.kwargs['explicit_json'], False



# Generated at 2022-06-13 22:05:07.171184
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(format_options={'json': {'format': True, 'sort_keys': True, 'indent': True}})
    mime = 'json'
    body = '{"key1": "value1", "key2": "value2"}'
    assert body == formatter.format_body(body, mime)

# Generated at 2022-06-13 22:05:11.254740
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    jsonFormatter = JSONFormatter(format_options={
        "json": {
            "format": True,
            "sort_keys": False,
            "indent": 2
        }
    })
    assert jsonFormatter.enabled == True


# Generated at 2022-06-13 22:05:20.477802
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    plugin = JSONFormatter({'json': {'format': True, 'indent': 4, 'sort_keys': True}})
    
    # Test the case where body parameter is empty string
    assert plugin.format_body('', '') == ''

    # Test the case where body parameter is string representation of array
    assert plugin.format_body('["a", "b", "c"]', 'json') == '[\n    "a",\n    "b",\n    "c"\n]'

    # Test the case where body parameter is string representation of object
    assert plugin.format_body('{"one": 1, "two": 2, "three": 3}', 'json') == '{\n    "one": 1,\n    "three": 3,\n    "two": 2\n}'

    # Test the case where body parameter is string

# Generated at 2022-06-13 22:05:29.158266
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
        explicit_json=True)
    json_body = '{ "a": 1, "b": 2, "b": 3 }'
    expected = '{\n    "a": 1,\n    "b": 3\n}'
    mime = 'application/json'
    assert json_formatter.format_body(json_body, mime) == expected

# Generated at 2022-06-13 22:05:31.987276
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    new_JSONFormatter = JSONFormatter()
    assert isinstance(new_JSONFormatter, JSONFormatter)

# Generated at 2022-06-13 22:05:41.245043
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(format_options={
        'json': {
            'format': True,
            'indent': 2,
            'sort_keys': True
        }
    })
    test_cases = [
        ('text/plain', 'test', 'test'),
        ('application/json', '{"test": test}', '{\n  "test": "test"\n}'),
        ('application/javascript', '{"test": test}', '{\n  "test": "test"\n}'),
        ('application/text', '{"test": test}', '{\n  "test": "test"\n}')
    ]

    for case in test_cases:
        assert formatter.format_body(case[1], case[0]) == case[2]

# Generated at 2022-06-13 22:05:51.076096
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    def assert_format_body(body, mime, expected):
        formatter = JSONFormatter()
        actual = formatter.format_body(body, mime)
        assert actual == expected

    # Invalid JSON
    assert_format_body('{', 'application/json', '{')
    assert_format_body('"a"', 'application/json', '"a"')
    assert_format_body('{"a"', 'application/json', '{"a"')
    assert_format_body('{"a"}', 'application/json', '{"a"}')

    # Valid JSON
    assert_format_body(
        '{"a":1}',
        'application/json',
        '{\n    "a": 1\n}'
    )

# Generated at 2022-06-13 22:06:01.913664
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    class FakeJSONFormatter:
        def __init__(self, **kwargs):
            self.kwargs = kwargs
            self.format_options = {
                'json': {
                    'format': True
                }
            }

    json_formatter = JSONFormatter(**FakeJSONFormatter().kwargs)
    json_formatter.kwargs = {'explicit_json': False}
    body_with_valid_json = '{"key": "value", "is_valid": "yes"}'
    body_with_invalid_json = '{"key": "value", "is_valid": "no"}'

# Generated at 2022-06-13 22:06:09.029375
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    format_options = {
        "json": {"format": True, "sort_keys": True, "indent": 4}
    }
    test = JSONFormatter(format_options)
    assert not test.kwargs
    assert test.format_options == format_options
    assert test.enabled



# Generated at 2022-06-13 22:06:28.371195
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()

    # Body without valid JSON format
    text = "I'm not JSON"
    mime = 'text'
    expected_output = "I'm not JSON"
    output = formatter.format_body(text, mime)
    assert output == expected_output

    # Body with valid JSON format 
    text = '{"glossary":{"title":"example glossary","GlossDiv":{"title":"S","GlossList":{"GlossEntry":{"ID":"SGML","SortAs":"SGML","GlossTerm":"Standard Generalized Markup Language","Acronym":"SGML","Abbrev":"ISO 8879:1986","GlossDef":{"para":"A meta-markup language, used to create markup languages such as DocBook.","GlossSeeAlso":["GML","XML"]},"GlossSee":"markup"}}}}}'
    expected

# Generated at 2022-06-13 22:06:38.489282
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    body = '{"a": 1}'

    def mock_loads(value):
        return json.loads(value)

    def mock_dumps(obj, sort_keys=False, ensure_ascii=False, indent=0):
        body = json.dumps(obj=obj, sort_keys=False, ensure_ascii=False, indent=0)
        return body

    import __main__
    import httpie.plugins
    __main__.json = json
    json_ = __main__.json
    httpie.plugins.json = json
    httpie.plugins.__main__.json = json
    json = httpie.plugins.__main__.json

    import contextlib
    from unittest.mock import patch


# Generated at 2022-06-13 22:06:43.608861
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    x = JSONFormatter()
    # Empty string
    assert x.format_body("", "json") == ""
    # Invalid JSON
    assert x.format_body("{", "json") == "{}"
    # Valid JSON
    assert x.format_body("{}", "json") == "{\n}"
    # Valid Unicode JSON
    assert x.format_body("{\"\u26a0\":\"\u26a0\"}", "json") == "{\n    \"\\u26a0\": \"\\u26a0\"\n}"

# Generated at 2022-06-13 22:06:50.783059
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(
        format_options ={'json':{'format':True}},
        explicit_json =False)
    body = '{"message":"a test message"}'
    mime = 'json'
    body_expected = '{\n    "message": "a test message"\n}'
    format_body = formatter.format_body(body, mime)
    assert body_expected == format_body

# Generated at 2022-06-13 22:06:59.933489
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    options = {
        'json': {
            'format': True,
            'indent': 4,
            'sort_keys': False
        },
        'colors': {},
        'style': {
            'headers': 'none'
        }
    }
    kwargs = {
        'explicit_json': False,
        'format_options': options
    }
    formatter = JSONFormatter(**kwargs)

    mime = 'application/json'
    body = '{"a": 123, "b": false}'
    expected = '{\n    "a": 123,\n    "b": false\n}'
    assert formatter.format_body(body, mime) == expected

# Generated at 2022-06-13 22:07:05.334953
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    from httpie.plugins.builtin import BuiltinPluginManager
    manager = BuiltinPluginManager()
    manager.add_plugin(JSONFormatter)
    assert manager.get_plugin(key='json') != None, "manager.get_plugin(key='json') returns None"


# Generated at 2022-06-13 22:07:10.019712
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    assert JSONFormatter(format_options={'json': {'format': True}}).enabled
    assert JSONFormatter(format_options={'json': {'format': False}}).enabled is False

# Generated at 2022-06-13 22:07:17.498563
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    body = b'{"user_id": 1, "user_name": "foo", "email": "foo@bar.com"}'
    mime = 'application/json'
    f = JSONFormatter()
    assert f.format_body(body.decode(), mime) == '{\n    "email": "foo@bar.com", \n    "user_id": 1, \n    "user_name": "foo"\n}'

# Generated at 2022-06-13 22:07:23.899987
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    import pytest
    json_formatter = JSONFormatter(explicit_json=False, format_options={'json': {'sort_keys': False, 'indent': 2, 'format': True}})
    assert(json_formatter.format_body('{ "key": "value" }', 'application/json') == '{ "key": "value" }')

test_JSONFormatter_format_body()

# Generated at 2022-06-13 22:07:32.741754
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    plugin = JSONFormatter(explicit_json=False, **{
        'format_options': {
            'json': {
                'sort_keys': True,
                'indent': 4,
            }
        }
    })
    plugin.enabled = True
    # Case 1: A valid json data
    data_json = '{"name":"httpie","age":9999}'
    mime = 'json'
    assert plugin.format_body(data_json, mime) == '''{
    "age": 9999,
    "name": "httpie"
}'''

