

# Generated at 2022-06-13 22:01:54.511383
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    """
    Get the JSON data first to make sure that the JSON is correct.
    Then use format_body method to convert the JSON data to string data.
    Finally, check whether the string data can trans back to the same JSON data.
    """
    import json
    test_json = {'key1':'value1','key2':'value2'}
    test_str = json.dumps(test_json)
    test_class = JSONFormatter()
    formatted_str = test_class.format_body(test_str, 'json')
    formatted_json = json.loads(formatted_str)
    assert test_json == formatted_json

# Generated at 2022-06-13 22:02:06.633392
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_mommy = JSONFormatter(options={'explicit_json': True},
                               format_options={'json': {'format': True,
                                                        'indent': 1,
                                                        'sort_keys': False}})

    json_string = '{"a":1,"b":2,"c":3,"d":"d"}'
    json_mommy.format_body(body=json_string, mime='json')
    # assert json_mommy.format_body(body=json_string, mime='json') == '{\n "a": 1,\n "b": 2,\n "c": 3,\n "d": "d"\n}'

# Generated at 2022-06-13 22:02:16.320444
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.plugins.JSONFormatterPlugin import JSONFormatter
    from io import BytesIO

    # Test normal cases
    body = '{"age":"1","name":"Bob"}'
    formatter = JSONFormatter(format_options={"json":{"format":True,"indent":4,"sort_keys":True}},explicit_json=False)
    assert formatter.format_body(body, 'json')=='{\n    "age": "1",\n    "name": "Bob"\n}'
    body = '{"name":"Bob","age":1}'
    assert formatter.format_body(body, 'javascript')=='{\n    "name": "Bob",\n    "age": 1\n}'

# Generated at 2022-06-13 22:02:29.227160
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    jf=JSONFormatter(format_options={'json':{'format':True, 'indent':0, 'sort_keys':True}}, explicit_json=True, json_indent=0, sort_keys=True)

    example_1={'mime':'application/json', 'body':'{"data": {"books": [{"id": 1, "title": "Brave New World", "authors": ["Aldous Huxley"]}, {"id": 2, "title": "1984", "authors": ["George Orwell"]}, {"id": 3, "title": "Fahrenheit 451", "authors": ["Ray Bradbury"]}]}}'}

# Generated at 2022-06-13 22:02:39.109747
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    f = JSONFormatter()
    class args:
        json = {'format': True, 'sort_keys': True, 'indent': 1}
        explicit_json = False
    f.set_kwargs(args)
    body = '{"a": 1, "b": {"c": "d"}}'
    mime = 'json'
    assert f.format_body(body, mime) == '{"a": 1, "b": {"c": "d"}}'

    body = '{"a": 1, "b": {"c": "d"}}'
    mime = 'application/json'
    assert f.format_body(body, mime) == '{"a": 1, "b": {"c": "d"}}'

    body = '{"a": 1, "b": {"c": "d"}}'


# Generated at 2022-06-13 22:02:47.795386
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_content = '{"name": "Francis", "nickname": "james"}'
    formatter = JSONFormatter()
    formatter.kwargs = {'explicit_json': True}
    formatter.format_options = {
        'json': {
            'format': True,
            'indent': 2,
            'sort_keys': True
        }
    }
    assert formatter.format_body(json_content, 'plain') == '{\n  "name": "Francis",\n  "nickname": "james"\n}'

# Generated at 2022-06-13 22:02:56.302818
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.core import ExitStatus
    from httpie import cli

    class TestingJsonFormatter(JSONFormatter):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.exception = None

        def format_body(self, *args):
            try:
                body = super().format_body(*args)
            except Exception as e:
                self.exception = e
            finally:
                return body

        def exit(self):
            raise ExitStatus.OK

    env = cli.Environment(stdin_isatty=True, stdout_isatty=True)
    args = cli.parser.parse_args([])
    json_formatter = TestingJsonFormatter(env, args)

    # Valid JSON
    body

# Generated at 2022-06-13 22:03:07.706484
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(**{
        "format_options": {
            "json": {
                "format": False,
                "indent": None,
                "sort_keys": False,
            }
        }
    })
    mime = "application/json"

# Generated at 2022-06-13 22:03:20.932649
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        json_file = temp_dir + '/test_JSONFormatter_format_body.json'
        if not json_file.endswith('.json'):
            json_file = json_file + '.json'

        # create empty file
        with open(json_file, 'w') as f:
            f.write("invalid json")

        with open(json_file, 'r') as f:
            j_formatter = JSONFormatter(explicit_json=True, stdout=f)
            f.seek(0)
            j_formatter.format_body(f.read(), 'json')


# j_formatter = JSONFormatter(explicit_json=True)
# assert j_formatter.format_body(
#

# Generated at 2022-06-13 22:03:34.379280
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    fp = JSONFormatter(
        format_options=dict(
            json=dict(
                format=True,
                sort_keys=False,
                indent=2
            )
        )
    )
    assert (fp.format_body(body='{"a": 1}', mime='application/json')
            == '{\n  "a": 1\n}')
    assert (fp.format_body(body='{"a": 1}', mime='text/html')
            == '{\n  "a": 1\n}')
    assert (fp.format_body(body='<html><body>', mime='text/html')
            == '<html><body>')
    assert (fp.format_body(body='invalid JSON', mime='application/json')
            == 'invalid JSON')

# Generated at 2022-06-13 22:03:52.477139
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # test 1
    json_formatter = JSONFormatter(explicit_json=True,
                                   format_options={
                                    'json': {
                                         'format': True,
                                         'indent': 2,
                                         'sort_keys': False
                                        }
                                    })
    assert json_formatter.format_body(
        body='{"key1": "value1", "key2": "value2"}',
        mime='json') == '{\n  "key1": "value1",\n  "key2": "value2"\n}'

# Generated at 2022-06-13 22:04:02.878422
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.cli import parse_items
    from httpie.client import HTTPie
    from httpie.compat import str
    from httpie.output import OutputOptions
    from httpie.output.streams import STDOUT
    from httpie.plugins import FORMATTERS
    from httpie.plugins.builtin import JSONOptions
    from httpie.plugins.json import JSONFormatter

    # Parse options.
    filters = dict()
    opts = dict()
    headers = dict()
    output_options = OutputOptions(
        json=JSONOptions(
            format=True,
            indent=None,
            sort_keys=False
        )
    )

# Generated at 2022-06-13 22:04:12.770485
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()
    json_str = '{"foo":"bar","baz":"qux"}'
    assert formatter.format_body(
        json_str,
        'application/json'
    ) == json_str

    # JSON is not reformatted if the Content-Type is text/plain
    assert formatter.format_body(
        json_str,
        'text/plain'
    ) == json_str

    # JSON is reformatted, if explicit_json is set to True
    assert formatter.format_body(
        json_str,
        'text/plain',
        explicit_json=True
    ) == json.dumps(
        json.loads(json_str),
        indent=4
    )

    # Invalid JSON is not reformatted

# Generated at 2022-06-13 22:04:26.395448
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.plugins import FormatterPlugin
    from httpie.ui import JSON_FORMATTER_OPTIONS
    from httpie import __version__
    from httpie.models import Environment
    import json
    import mimetypes
    import requests
    import pprint

    # FormatterPlugin.__init__(self)

# Generated at 2022-06-13 22:04:37.404411
# Unit test for method format_body of class JSONFormatter

# Generated at 2022-06-13 22:04:46.365270
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    body = '{"hello": "world", "foo": 42, "bar": {"baz": "foobar"}}'
    import json
    correct_output = json.dumps(
        obj=json.loads(body),
        sort_keys=False,
        ensure_ascii=False,
        indent=2
    )
    assert correct_output == JSONFormatter(format_options={'json': {'format': True, 'indent': 2, 'sort_keys': False}}, explicit_json=False).format_body(body, 'application/json')

# Generated at 2022-06-13 22:04:51.362016
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    jf = JSONFormatter(format_options={
        'json': {
            'sort_keys': False,
            'indent': 1,
            'format': True
        }
    })
    assert jf.format_body("{'a': 1}", 'text') == '{\n "a": 1\n}'

# Generated at 2022-06-13 22:05:01.557178
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.plugins import FormatterPlugin
    from json import loads
    from json import dumps
    kwargs = {'explicit_json': True,
              'skip': False,
              'headers': True,
              'style': 'AUTO',
              'stream': False,
              'body_max_size': 1048576,
              'verbose': False,
              'print_body': True,
              'json': {'format': True,
                       'indent': 2,
                       'sort_keys': False},
              'colors': True,
              'format_options': {'json': {'indent': True,
                                          'sort_keys': False,
                                          'format': True}}}
    x = FormatterPlugin(**kwargs)
    y = JSONFormatter(**kwargs)
    # Test

# Generated at 2022-06-13 22:05:13.468870
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    obj1 = {
        'foo': 'bar',
        'alice': 'bob'
    }

    obj2 = {
        'foo': 'bar',
        'alice': 'bob',
    }

    body1 = json.dumps(
        obj=obj1,
        sort_keys=True,
        ensure_ascii=False,
        indent=2
    )

    body2 = json.dumps(
        obj=obj2,
        sort_keys=True,
        ensure_ascii=False,
        indent=2
    )

    json_formatter = JSONFormatter(explicit_json=True)
    assert json_formatter.format_body(body=body1, mime='text') == body2

# Generated at 2022-06-13 22:05:20.746588
# Unit test for method format_body of class JSONFormatter

# Generated at 2022-06-13 22:05:26.854094
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter()

    # Test case: invalid JSON, ignore.
    assert json_formatter.format_body(
        body='abcde', mime='application/json'
    ) == 'abcde'

    # Test case: valid JSON, indent, sort keys by name.
    assert json_formatter.format_body(
        body='{"b":1, "a":2}', mime='application/json'
    ) == '{\n    "a": 2,\n    "b": 1\n}'

# Generated at 2022-06-13 22:05:31.205966
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Arrange
    formatter = JSONFormatter()
    body = '{"hello": "world"}'
    mime = 'json'
    expected = '{\n    "hello": "world"\n}'
    # Act
    actual = formatter.format_body(body, mime)
    # Assert
    assert actual == expected

test_JSONFormatter_format_body()

# Generated at 2022-06-13 22:05:43.855936
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(colors=False, format_options={'json': {'format': True, 'sort_keys': True, 'indent': 4}})
    resp = {"foo": "bar", "baz": "qux"}
    json_str = json.dumps(resp, sort_keys=True, indent=4)
    assert formatter.format_body(json.dumps(resp), 'json') == json_str
    assert formatter.format_body(json.dumps(resp), 'javascript') == json_str
    assert formatter.format_body(json.dumps(resp), 'text') == json_str
    assert formatter.format_body("foo bar", 'text') == 'foo bar'

# Generated at 2022-06-13 22:05:49.643466
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # mock class
    class Mock:
        pass

    formatter = JSONFormatter(
        Mock()
        , Mock()
        , Mock()
        , explicit_json = False
    )

    body = '{"a":"A"}'
    mime = 'json'
    if formatter.format_body(body, mime) != body:
        raise AssertionError(formatter.format_body(body, mime))

# Generated at 2022-06-13 22:06:01.180242
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.plugins.builtin import JSONJSON

    # Default options.
    formatter = JSONFormatter(
        JSONJSON(indent=2, sort_keys=False, explicit_json=False))
    assert formatter.format_body(
        '{"a": "b", "c": "d"}', 'application/json') == '{\n  "a": "b",\n' \
        '  "c": "d"\n}'

    # Test explicit json.
    formatter = JSONFormatter(
        JSONJSON(indent=2, sort_keys=False, explicit_json=True))

# Generated at 2022-06-13 22:06:13.558924
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # create JSONFormatter object
    json_formatter = JSONFormatter()
    # test invalid JSON object
    assert json_formatter.format_body('{"key": "value",}', 'application/json') is not None
    # test valid JSON object
    assert json_formatter.format_body('{"key": "value"}', 'application/json') is not None
    # test JSON object without sorting keys
    assert json_formatter.format_body('{"key": "value"}', 'application/json') is not None
    # test JSON object with sorting keys
    json_formatter.format_options['json']['sort_keys'] = True
    assert json_formatter.format_body('{"key": "value"}', 'application/json') is not None
    # test JSON object without indentation
    json_formatter.format_options

# Generated at 2022-06-13 22:06:24.821745
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    body = '{"foo": "bar"}'
    formatter = JSONFormatter(format_options={'json': {'format': True, 'sort_keys': False, 'indent': 4}})
    assert formatter.format_body(body=body, mime='application/json') == '{\n    "foo": "bar"\n}'
    formatter = JSONFormatter(format_options={'json': {'format': False, 'sort_keys': False, 'indent': 4}})
    assert formatter.format_body(body=body, mime='application/json') == body
    formatter = JSONFormatter(format_options={'json': {'format': True, 'sort_keys': False, 'indent': 4}})
    assert formatter.format_body(body=body, mime='text/plain')

# Generated at 2022-06-13 22:06:34.132384
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    import argparse
    from httpie.context import Environment

    env = Environment(argparse.Namespace())

    json_plugin = JSONFormatter(env)
    body = "abcd"
    mime = "json"
    assert json_plugin.format_body(body, mime) == "abcd"

    json_plugin = JSONFormatter(env)
    body = "{\"a\": 1}"
    mime = "json"
    assert json_plugin.format_body(body, mime) == body


if __name__ == '__main__':
    import pytest
    pytest.main()

# Generated at 2022-06-13 22:06:41.425199
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    jf = JSONFormatter()
    jf.kwargs = {
        'explicit_json': False,
    }
    jf.format_options = {
        'json': {
            'format': True,
            'sort_keys': True,
            'indent': 2,
        },
    }
    # Test that the body is converted from JSON
    body = '{"foo": "bar"}'
    mime = 'json'
    assert jf.format_body(body, mime) == '{\n  "foo": "bar"\n}'
    # Test that the body is not converted
    body = '<!DOCTYPE html><HTML><BODY>Hello!</BODY></HTML>'
    mime = 'html'

# Generated at 2022-06-13 22:06:54.218306
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Unit test: JSONFormatter.format_body()
    formatter = JSONFormatter(
        __config__=None,
        __file__=None,
        __name__=None,
        __package__=None,
        format_options={
            'json': {
                'format': True,
                'indent': 4,
                'sort_keys': False,
            }
        },
        explicit_json=False,
    )

    maybe_json = [
        'json',
        'javascript',
        'text',
    ]

    assert formatter.format_body('{"test": "name"}', 'json') == '''{
    "test": "name"
}'''


# Generated at 2022-06-13 22:07:10.650084
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    f = JSONFormatter()
    body = '{"project": {"id": 123456789, "name": "My project"}}'

    with_json_mimetype = f.format_body(body, 'application/json')
    assert body == with_json_mimetype
    assert body == '{\n    "project": {\n        "id": 123456789,' \
           ' \n        "name": "My project"\n    }\n}'

    with_text_mimetype = f.format_body(body, 'text/plain')
    assert body == with_text_mimetype
    assert body == '{\n    "project": {\n        "id": 123456789,' \
           ' \n        "name": "My project"\n    }\n}'

    wrong

# Generated at 2022-06-13 22:07:21.122807
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    print('\n[Test] JSONFormatter.format_body()')
    jf = JSONFormatter()
    body = '{"a":2, "b":3}'
    mime = 'application/json'
    print('[test1] input: {}'.format(body))
    print('[test1] mime: {}'.format(mime))
    fbody = jf.format_body(body, mime)
    print('[test1] output: {}'.format(fbody))

if __name__ == '__main__':
    test_JSONFormatter_format_body()

# Generated at 2022-06-13 22:07:24.698191
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter()
    body = "{'key': 'value'}"
    mime = 'json'
    result = json_formatter.format_body(body, mime)
    expected = '{\n    "key": "value"\n}'
    assert result == expected

# Generated at 2022-06-13 22:07:35.717800
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():

    # Success case 1: body is JSON in encoding utf-8
    formatter = JSONFormatter(explicit_json=False, format_options={'json': {'format': 'on', 'indent': 4, 'sort_keys': 'on'}})
    # body is JSON string in encoding utf-8
    body = '{"id": 1, "name": "TEST"}'
    mime = 'application/json'
    assert formatter.format_body(body, mime) == '{\n    "id": 1,\n    "name": "TEST"\n}'
    # body is text string in encoding utf-8
    body = '{"id": 1, "name": "TEST"}'
    mime = 'text/plain'

# Generated at 2022-06-13 22:07:45.752722
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    obj = {
        'key_1': 'value_1',
        'key_2': 'value_2',
        'key_3': 'value_3',
    }
    json_obj = '{\n  "key_1": "value_1",\n  "key_2": "value_2",\n  "key_3": "value_3"\n}'
    assert json_obj == json.dumps(
        obj=obj,
        sort_keys=True,
        ensure_ascii=False,
        indent=2
    )


# Generated at 2022-06-13 22:07:53.204768
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(format_options={
                                  'json': {
                                      'format': False,
                                      'indent': True,
                                      'sort_keys': False
                                  }
                              })
    json_str = '{"name": "httpie"}'
    assert formatter.format_body(json_str, 'json') == json_str

# Generated at 2022-06-13 22:08:07.634101
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    """
    Test suite for format_body method of class JSONFormatter
    """
    import io
    import sys
    import unittest
    import httpie.output.formatters
    from httpie.output.formatters import JSONFormatter
    from httpie.plugins import FormatterPlugin
    from httpie.plugins import FormatterPlugin
    
    class DummyResponse:
        def __init__(self, body=None, headers=None, status_code=None):
            self.body = body
            self.headers = headers
            self.status_code = status_code
            

# Generated at 2022-06-13 22:08:19.279332
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Test.
    test_json_formatter = JSONFormatter(format_options={
            'json': {
                'format': True,
                'explicit': False,
                'sort_keys': True,
                'indent': 2
            }
        })

    assert test_json_formatter.format_body(
        body='{"key": "value"}',
        mime='application/json'
    ) == '{\n  "key": "value"\n}'

    # Test.
    test_json_formatter = JSONFormatter(format_options={
            'json': {
                'format': True,
                'explicit': False,
                'sort_keys': True,
                'indent': 2
            }
        })


# Generated at 2022-06-13 22:08:30.568742
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    plugin = JSONFormatter(no_color=True, format_options=dict(
        json=dict(format=True, indent=2, sort_keys=False)))
    body = '{"foo": "bar", "baz": {"qux": "quux"}}'
    assert plugin.format_body(body, 'application/json') == '''{
  "baz": {
    "qux": "quux"
  },
  "foo": "bar"
}'''
    body = '{"foo": "bar", "baz": {"qux": "quux"}}'
    assert plugin.format_body(body, 'text/javascript') == '''{
  "baz": {
    "qux": "quux"
  },
  "foo": "bar"
}'''

# Generated at 2022-06-13 22:08:38.686418
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    data = '{"name": "John", "age": 30, "car": null}'
    json_plugin = JSONFormatter({'json': {'indent': 4}})
    data_formatted = json_plugin.format_body(data, 'json')
    assert data_formatted == '{\n    "name": "John",\n    "age": 30,\n    "car": null\n}'

# Generated at 2022-06-13 22:09:00.262698
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Instantiate object
    fp = JSONFormatter({'json': {'indent': 2, 'format': True, 'sort_keys': True}},
            {'explicit_json': False})

    # Sample valid JSON strings
    sample_json_1 = '''{
        "a": "b",
        "c": "d",
        "e": "f"
    }'''
    sample_json_2 = '''{
        "a": "xyz",
        "c": "abc"
    }'''

    # Sample invalid JSON string
    sample_json_invalid = '{"a": "b", "c": "d", "e": "f"}'

    # Formatted sample JSON strings

# Generated at 2022-06-13 22:09:09.669042
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():

    correct_1 = '''{
    "name": "John Doe",
    "age": 30,
    "wife": {
        "name": "Jane Doe",
        "age": 30
    }
}'''

    correct_2 = '''{
    "name": "John Doe",
    "age": 30,
    "wife": {
        "name": "Jane Doe",
        "age": 30
    }
}'''

    correct_3 = '''{
    "name": "John Doe",
    "wife": {
        "name": "Jane Doe",
        "age": 30
    },
    "age": 30
}'''

    # no need to sort keys

# Generated at 2022-06-13 22:09:12.786452
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    JSONFormatter.format_body('{"key":"value"}', 'json')
    JSONFormatter.format_body('{"key":"value"}', 'javascript')
    JSONFormatter.format_body('{"key":"value"}', 'text')
    JSONFormatter.format_body('{"key":"value"}', 'text/plain')

# Generated at 2022-06-13 22:09:22.965053
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    content = '{"key": "value"}'
    formatter = JSONFormatter()

    # Input: JSON, expected output: Indented JSON
    json_indent = formatter.format_body(content, 'json')
    assert json_indent
    assert (json_indent == '{\n'
                           '    "key": "value"\n'
                           '}'
                           )

    # Input: "application/javascript", expected output: Indented JSON
    javascript_indent = formatter.format_body(content, 'javascript')
    assert javascript_indent
    assert (javascript_indent == '{\n'
                                 '    "key": "value"\n'
                                 '}'
                                 )

    # Input: "text/plain", expected output: JSON (should be same as input)
    text

# Generated at 2022-06-13 22:09:32.122307
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    class MockJSONFormatter(JSONFormatter):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

    json_formatter = MockJSONFormatter(
        format_options={'json': {
            'sort_keys': False,
            'indent': 2,
            'format': True
        }},
        explicit_json=False
    )

    # Body with valid JSON but on the wrong format (indent or sort)
    body = '{\n\t"foo": "bar"\n\n}'
    assert json_formatter.format_body(body, 'application/json') == '{\n  "foo": "bar"\n}'

    # Body with valid JSON format and correct JSON format
    body = '{\n\t"foo": "bar"\n}'

# Generated at 2022-06-13 22:09:37.423482
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_obj = json.dumps({'success': True})
    formatter = JSONFormatter({'json': {'sort_keys' : True, 'indent' : 4}})
    output = formatter.format_body(json_obj, 'json')
    assert json.loads(output)['success'] == True

# Generated at 2022-06-13 22:09:44.579180
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(format_options={
        'json': {
            'format': True,
            'sort_keys': True,
            'indent': 4
        }
    }, explicit_json=True)
    assert formatter.format_body('{"a": 1, "b": 2}', '') == \
        '{\n    "a": 1,\n    "b": 2\n}'

# Generated at 2022-06-13 22:09:57.290985
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    jf = JSONFormatter(format_options={
        "json": {
            "format": True,
            "indent": 1,
            "sort_keys": True
        }
    },
                                   explicit_json=False)

    expected = '{\n "test": "success"\n}'
    actual = jf.format_body('{"test":"success"}', 'mime')
    assert actual == expected

    expected = '{"test":"success"}'
    actual = jf.format_body('{"test":"success"}', 'mime/json')
    assert actual == expected

    expected = '{"test":"success"}'
    actual = jf.format_body('{bad: json}', 'mime/json')
    assert actual == expected

# Generated at 2022-06-13 22:10:05.925326
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    class TmpUser:
        def __init__(self, name: str, age: int):
            self.name = name
            self.age = age

    formatter = JSONFormatter()
    formatter.set_format_options(format='all')

    # Explicit json.
    assert formatter.format_body(
        body=json.dumps({'a': 1, 'b': 2}),
        mime='application/json',
    ) == '{\n    "a": 1,\n    "b": 2\n}'

    # JSON-stringified object.
    assert formatter.format_body(
        body='{"a": 1, "b": 2}',
        mime='text/plain',
    ) == '{\n    "a": 1,\n    "b": 2\n}'

   

# Generated at 2022-06-13 22:10:15.480508
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.response.human import JSON_SORT_KEYS
    json_formatter = JSONFormatter(json={'format': True,
                                         'sort_keys': JSON_SORT_KEYS})
    json_formatter.kwargs['explicit_json'] = True
    assert json_formatter.format_body(
        body="""{"a": 1, "b": 2}""",
        mime="application/json"
    ).strip() == """{
  "a": 1,
  "b": 2
}"""
    assert json_formatter.format_body(
        body="""{"a": 1, "b": 2}""",
        mime="text/javascript"
    ).strip() == """{
  "a": 1,
  "b": 2
}"""

# Generated at 2022-06-13 22:10:36.675308
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    assert True

# Generated at 2022-06-13 22:10:41.692783
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(
        format_options={
            'json': {
                'format': True,
                'indent': 4,
                'sort_keys': True,
            }
        },
        explicit_json=False
    )
    body = '{"key1": "value1", "key2": "value2"}'
    assert formatter.format_body(body=body, mime='json') == \
        '{\n' \
        '    "key1": "value1",\n' \
        '    "key2": "value2"\n' \
        '}'

# Generated at 2022-06-13 22:10:43.412133
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    assert False


# Generated at 2022-06-13 22:10:53.121015
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_fmt = JSONFormatter()
    assert json_fmt.format_body(
        '{"key":"value"}', "application/json") == '{\n    "key": "value"\n}'
    assert json_fmt.format_body(
        '{"key":"value"}', "application/javascript") == '{\n    "key": "value"\n}'
    assert json_fmt.format_body(
        '{"key":"value"}', "text/plain") == '{\n    "key": "value"\n}'
    assert json_fmt.format_body(
        '{"key":"value"}', "text/html") == '{"key":"value"}'

# Generated at 2022-06-13 22:10:57.832324
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    example_json = '{"version": 1.0, "count": 5, "desc": "example json"}'
    # Check that valid json is not altered.
    formatter = JSONFormatter()
    assert formatter.format_body(example_json, '') == example_json
    # Check that strings that are not json are not altered.
    assert formatter.format_body('Hello', '') == 'Hello'
    assert formatter.format_body('', '') == ''



# Generated at 2022-06-13 22:11:02.895896
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    jsonFormatter = JSONFormatter(**kwargs)
    body = '{"name":"Jeff Da Silva","age":11}'
    assert jsonFormatter.format_body(body) == '{\n  "age": 11, \n  "name": "Jeff Da Silva"\n}'

# Generated at 2022-06-13 22:11:13.550892
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    """Test method format_body of class JSONFormatter"""
    jsonformatter = JSONFormatter(**{'explicit_json': False, 'format_options': {'json': {'format': False, 'indent': 2, 'sort_keys': False}}})
    assert jsonformatter.format_body('{"test": 1}', 'application/json') == '{\n  "test": 1\n}'
    assert jsonformatter.format_body('{"test": 1}', 'application/javascript') == '{\n  "test": 1\n}'
    assert jsonformatter.format_body('{"test": 1}', 'text') == '{\n  "test": 1\n}'
    assert jsonformatter.format_body('{"test": 1}', 'text/xml') == '{"test": 1}'

# Generated at 2022-06-13 22:11:23.010801
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(json={'format': True, 'indent': 0, 'sort_keys': False})
    json_body = '[{"http": "//httpie.org"}, null, [1, 2]]'
    formatted_body = formatter.format_body(json_body, 'application/json')
    assert formatted_body != json_body
    assert formatted_body == '[{"http": "//httpie.org"}, null, [1, 2]]'

# Generated at 2022-06-13 22:11:25.421490
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    result = JSONFormatter().format_body('{"hello": "world"}', 'application/json')
    assert result == '{\n    "hello": "world"\n}'

# Generated at 2022-06-13 22:11:36.628855
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    '''
    NOTE: This is done for a *specific* desired functionality of this method.
    This does not necessarily test everything the method is supposed to do.
    '''
    test_formatter = JSONFormatter(format_options={
            'json': {
                'format': True,
                'indent': 4,
                'sort_keys': True
                }
            })

    # Test 1: blank string
    result = test_formatter.format_body('', 'json')
    assert result == ''

    # Test 2: invalid JSON string
    result = test_formatter.format_body('{"hello": "world"', 'json')
    assert result == '{"hello": "world"'

    # Test 3: valid JSON string with explicit json flag
    input_str = '{"hello": "world"}'
    result = test_form