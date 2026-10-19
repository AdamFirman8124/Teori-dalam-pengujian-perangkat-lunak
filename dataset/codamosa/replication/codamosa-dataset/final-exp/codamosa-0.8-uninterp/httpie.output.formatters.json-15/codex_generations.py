

# Generated at 2022-06-13 22:01:46.423957
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    assert JSONFormatter is not None

# Generated at 2022-06-13 22:01:48.149627
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    assert JSONFormatter({'json': {'format': True}})

# Generated at 2022-06-13 22:01:57.486848
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Create instance of JSONFormatter
    json_formatter = JSONFormatter()

    # Test that format_body interprets and formats correctly properly formatted json string
    # '{"a":1,"b":2}'
    body = '{"a":1,"b":2}'
    json_formatter.format_options['json']['format'] = True
    json_formatter.format_options['json']['sort_keys'] = False
    json_formatter.format_options['json']['indent'] = False
    assert json_formatter.format_body(body, 'application/json') == body

    # Test that format_body interprets and formats correctly badly formatted json string
    # '{"a":1,"b":2'
    json_formatter.format_options['json']['format'] = True
    json_

# Generated at 2022-06-13 22:02:08.960101
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    jf = JSONFormatter()
    jf.kwargs = {}
    assert jf.format_body(body="{}", mime="stuff") == "{}"
    assert jf.format_body(body="{}", mime="json") == "{}"
    assert jf.format_body(body="{}", mime="text/json") == "{}"
    assert jf.format_body(body="{}", mime="javascript") == "{}"
    assert jf.format_body(body="{}", mime="text/javascript") == "{}"
    assert jf.format_body(body="{}", mime="text") == "{}"
    assert jf.format_body(body="{}", mime="text/plain") == "{}"

# Generated at 2022-06-13 22:02:16.384512
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formater = JSONFormatter(format_options={'json':{'format': False}})
    payload = {'a':1, 'b':2}
    assert json_formater.format_body(json.dumps(payload), 'application/json') == json.dumps(payload)

    json_formater = JSONFormatter(format_options={'json':{'format': True}})
    assert json_formater.format_body(json.dumps(payload), 'application/json') == json.dumps(payload, indent=2)

    payload = '{a:1, b:2}'
    assert json_formater.format_body(payload, 'application/json') == payload

# Generated at 2022-06-13 22:02:24.577018
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter()
    # format_options = {
    #     "json": {
    #         "format": True,
    #         "indent": 2,
    #         "sort_keys": False
    #     }
    # }

    # JSON body and mime-type
    json_body = '{"key": "value"}'
    json_mime = 'application/json'
    formatted_body = json_formatter.format_body(json_body, json_mime)
    assert json.dumps({"key": "value"}, ensure_ascii=False, indent=2) == formatted_body
    # print(formatted_body)

    # JSON body with ternary

# Generated at 2022-06-13 22:02:34.060685
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():

        from httpie.compat import is_py26

        assert JSONFormatter.format_body(
            '{"a":1}',
            'application/json'
        ) == '{\n    "a": 1\n}'

        assert JSONFormatter.format_body(
            '{"a":1}',
            'text/json'
        ) == '{\n    "a": 1\n}'

        assert JSONFormatter.format_body(
            '{"a":1}',
            'application/javascript'
        ) == '{\n    "a": 1\n}'

        assert JSONFormatter.format_body(
            '{"a":1}',
            'application/xml'
        ) == '{"a":1}'


# Generated at 2022-06-13 22:02:44.758252
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # test for content type: application/json
    formatter = JSONFormatter()
    body = '{"spam":1,"eggs":2}'
    mime = 'application/json'
    assert formatter.format_body(body, mime) == '{\n    "eggs": 2,\n    "spam": 1\n}'
    # test for content type: text/javascript
    mime = 'text/javascript'
    assert formatter.format_body(body, mime) == '{\n    "eggs": 2,\n    "spam": 1\n}'
    # test for content type: text/plain
    mime = 'text/plain'

# Generated at 2022-06-13 22:02:51.499943
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    ## Setup test
    formatter = JSONFormatter()
    body = '{"name":"foo","status":"success","count":100}'
    mime = 'application/json'
    ## Execute test
    result = formatter.format_body(body, mime)
    ## Assert test
    assert result == '{\n    "count": 100,\n    "name": "foo",\n    "status": "success"\n}'

# Generated at 2022-06-13 22:03:01.678474
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()
    assert formatter.format_body('{"a": 1, "b": 2}\n{"a": 3, "b": 4}', 'application/json') == '{\n    "a": 1,\n    "b": 2\n}\n{\n    "a": 3,\n    "b": 4\n}\n'
    assert formatter.format_body('application/json', 'application/json') == 'application/json'
    assert formatter.format_body('{"a": 1, "b": 2}', 'application/json') == '{\n    "a": 1,\n    "b": 2\n}'

# Generated at 2022-06-13 22:03:08.554932
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    test = JSONFormatter()
    try:
        assert test.enabled == True
    except AssertionError:
        print("Failed the test_JSONFormatter unit test, try again")


# Generated at 2022-06-13 22:03:21.059455
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    """
    Tests the format_body method of the JSONFormatter
    """

# Generated at 2022-06-13 22:03:31.028053
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    jf = JSONFormatter(format_options={
        "json": {
            "format": True,
            "sort_keys": True,
            "indent": 4
        }
    }, explicit_json=True)
    assert jf.format_options['json']['format']
    dic = {'some': 'thing'}
    assert jf.format_body(json.dumps(dic), 'json') == json.dumps(
        dic,
        sort_keys=True,
        ensure_ascii=False,
        indent=4,
    )

# Generated at 2022-06-13 22:03:42.283478
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    expected = (
        '{\n'
        '    "course": "FMC",\n'
        '    "credit": 3,\n'
        '    "name": "Formal Methods Course",\n'
        '    "number": "626",\n'
        '    "term": "Fall",\n'
        '    "year": 2017\n'
        '}'
    )

    formatter = JSONFormatter()
    assert formatter.format_body(
        body='{"course": "FMC", "credit": 3, "name": "Formal Methods Course",'
             '"number": "626", "term": "Fall", "year": 2017}',
        mime='json'
    ) == expected


# Generated at 2022-06-13 22:03:47.478976
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    kwargs = {
        'json': {
            'sort_keys': True,
            'indent': 4,
            'format': True,
        },
        'explicit_json': False,
    }
    formatter = JSONFormatter(**kwargs)
    assert formatter.enabled

# Generated at 2022-06-13 22:03:59.914196
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(format_options={'json': {
        'format': True,
        'indent': 2,
        'sort_keys': True,
    }})
    body = '{"a": 1}'
    formatted_body = formatter.format_body(body=body, mime='json')
    assert formatted_body == '{\n  "a": 1\n}'
    body = '{"a": 1}'
    formatted_body = formatter.format_body(
        body=body,
        mime='application/json')
    assert formatted_body == '{\n  "a": 1\n}'
    body = '{"a": 1}'
    formatted_body = formatter.format_body(
        body=body,
        mime='text/javascript')
    assert formatted_body

# Generated at 2022-06-13 22:04:03.280195
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    formatter = JSONFormatter(format_options={'json': {'format': True, 'indent': 2, 'sort_keys': True}})


# Generated at 2022-06-13 22:04:10.739985
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()

    response_data = {
        "author": "HTTPie",
        "content": "HTTPie is a CLI, cURL-like tool for humans."
    }

    assert formatter.format_body(json.dumps(response_data), 'json') == '{\n    "author": "HTTPie",\n    "content": "HTTPie is a CLI, cURL-like tool for humans."\n}'



# Generated at 2022-06-13 22:04:16.382458
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    assert JSONFormatter.format_body('{"a":1}', None) == '{"a": 1}'
    assert JSONFormatter.format_body('{"a":1}', 'json') == '{"a": 1}'
    assert JSONFormatter.format_body('{"c":3, "b":2, "a":1}', 'json') == '{\n    "a": 1,\n    "b": 2,\n    "c": 3\n}'

# Generated at 2022-06-13 22:04:28.381589
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    def helper_format_body(mime, json_string):
        class HTTPieTest:
            def __init__(self, mime, json_string):
                self.kwargs = {
                    'explicit_json': False,
                }
                self.format_options = {
                    'json': {
                        'format': True,
                        'sort_keys': True,
                        'indent': 4,
                    }
                }
                self.mime = mime
                self.json_string = json_string
                self.expected_string = json.dumps(
                    obj=json.loads(json_string),
                    sort_keys=True,
                    ensure_ascii=False,
                    indent=4
                )

        test = HTTPieTest(mime, json_string)

# Generated at 2022-06-13 22:04:43.595940
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    test_body = '{"b":2, "a":1}'
    assert test_body == JSONFormatter({'json.format': True}).format_body(test_body, 'json')
    assert '{\n  "a": 1,\n  "b": 2\n}' == JSONFormatter({'json.format': True, 'json.indent': 2}).format_body(test_body, 'json')
    assert '{\n    "a": 1,\n    "b": 2\n}' == JSONFormatter({'json.format': True, 'json.indent': 4}).format_body(test_body, 'json')
    assert test_body == JSONFormatter({'json.format': False}).format_body(test_body, 'json')

# Generated at 2022-06-13 22:04:54.383483
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.plugins.json import JSONFormatter
    from httpie.plugins.builtin import BodyFormatterPlugin

    request = {
        'headers': '',
        'url': '',
        'method': 'GET',
        'body':
            '{ "color": "red", '
            '"value": "#f00" }'
    }

    format_options = {
        'json': {
            'format': True,
            'indent': 4,
            'sort_keys': True,
        },
    }

    httpie_args = ["--ignore-stdin", "--print", "bBH", request['method'], "--json", request['url']]
    body_formatter = BodyFormatterPlugin()

# Generated at 2022-06-13 22:04:59.823928
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    from httpie.plugins import FormatterPlugin
    formatter = FormatterPlugin(
        explicit_json=False,
        format_options={
            'json' : {
                'format': True,
                'indent': 4,
                'sort_keys': True,
            },
            'colors': {
                'lookup': 'auto'
            }
        }
    )
    assert formatter.enabled == True



# Generated at 2022-06-13 22:05:04.917771
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(format_options = {'json': {'format': True, 'sort_keys': True, 'indent': 4}})
    body = '{"key":"val"}'
    mime = 'json'
    assert formatter.format_body(body, mime) == '''{
    "key": "val"
}'''

    formatter = JSONFormatter(format_options = {'json': {'format': False, 'sort_keys': True, 'indent': 4}})
    assert formatter.format_body(body, mime) == body

# Generated at 2022-06-13 22:05:10.121620
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.plugins.formatter.json import JSONFormatter
    from httpie.plugins.core import FormatterPlugin
    from httpie.context import Environment

    json_formatter = JSONFormatter(Environment())
    formatter_plugin = FormatterPlugin(Environment())

    assert json_formatter.format_body('{}', 'json') == '{\n}'
    assert json_formatter.format_body('{}', 'javascript') == '{\n}'
    assert json_formatter.format_body('{}', 'text') == '{\n}'

    assert json_formatter.format_body('a', 'json') == 'a'
    assert json_formatter.format_body('a', 'javascript') == 'a'
    assert json_formatter.format_body('a', 'text') == 'a'



# Generated at 2022-06-13 22:05:12.988644
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    formatter = JSONFormatter(format_options={
        "json": {
            "format": True,
            "indent": 3,
            "sort_keys": True
        }
    })
    assert formatter.enabled


# Generated at 2022-06-13 22:05:20.536194
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    class SpecialPlugin:
        def __init__(self):
            self.kwargs = {
                'explicit_json': True
            }
            self.format_options = {
                'json': {
                    'format': True,
                    'sort_keys': True,
                    'indent': 2
                }
            }

    def check_format_body(body, mime):
        F = JSONFormatter(**SpecialPlugin().kwargs)

        # When format JSON
        F.enabled = True
        formatted_body = F.format_body(body, mime)
        assert(formatted_body != body)

        # When not format JSON
        F.enabled = False
        formatted_body = F.format_body(body, mime)
        assert(formatted_body == body)


# Generated at 2022-06-13 22:05:31.207138
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Test with body string and mime json
    formatter = JSONFormatter()
    assert formatter.format_body(
        '{"hello": "world"}',
        'application/json'
    ) == '{\n    "hello": "world"\n}'
    # Test with body string and mime javascript
    assert formatter.format_body(
        '{var json = {"hello": "world"}}',
        'text/javascript'
    ) == '{\n    "hello": "world"\n}'
    # Test with body string and mime text
    assert formatter.format_body(
        '{"hello": "world"}',
        'text/plain'
    ) == '{\n    "hello": "world"\n}'
    # Test with invalid json

# Generated at 2022-06-13 22:05:41.036672
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_str = '{"test": true}'
    formatter = JSONFormatter(kwargs={'explicit_json': True})
    assert formatter.format_body(body=json_str, mime='json') == json.dumps(json.loads(json_str), indent=2)
    assert formatter.format_body(body=json_str, mime='text') == json.dumps(json.loads(json_str), indent=2)
    assert formatter.format_body(body='\n' + json_str + '\n', mime='text') == '\n' + json.dumps(json.loads(json_str), indent=2) + '\n'

# Generated at 2022-06-13 22:05:51.075510
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    instance = JSONFormatter()

    instance.format_options = {'json' : {'format' : False}}
    assert instance.format_body('{"message" : "Hello World"}', 'text/json') == '{"message": "Hello World"}'

    instance.format_options = {'json' : {'format' : True}}
    assert instance.format_body('{"message" : "Hello World"}', 'text/json') == '{\n  "message": "Hello World"\n}'

    instance.format_options = {'json' : {'format' : False}}
    assert instance.format_body('{"message" : "Hello World"}', 'application/json') == '{"message": "Hello World"}'

    instance.format_options = {'json' : {'format' : True}}
    assert instance.format_

# Generated at 2022-06-13 22:06:07.090065
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    try:
        instance = JSONFormatter()
        assert isinstance(instance, JSONFormatter)
    except:
        assert False

# Generated at 2022-06-13 22:06:16.321347
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.output.formatters import JSONFormatter
    options = {
        "json": {
            "format": True,
            "indent": 2,
            "sort_keys": True
        }
    }
    import json
    body = "[1, 2, 3]"
    JSONFormatter().format_body(body=body, mime="application/json") == json.dumps([1, 2, 3], sort_keys=True, ensure_ascii=False, indent=2)
    body = "[1, 2, 3]"
    JSONFormatter().format_body(body=body, mime="application/javascript") == json.dumps([1, 2, 3], sort_keys=True, ensure_ascii=False, indent=2)
    body = "[1, 2, 3]"
    JSONFormatter().format

# Generated at 2022-06-13 22:06:24.345252
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()
    payload = '{"a": 1, "b": 2}'
    assert formatter.format_body(payload, 'json') == '{"a": 1, "b": 2}'
    assert formatter.format_body(payload, 'javascript') == '{"a": 1, "b": 2}'
    assert formatter.format_body(payload, 'text') == '{"a": 1, "b": 2}'

# Generated at 2022-06-13 22:06:36.052054
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.plugins import FormatterPlugin

    import unittest

    class TestJSONFormatter(unittest.TestCase):

        def setUp(self):
            self.kwargs = {'explicit_json': False}
            self.indent = 2
            self.sort_keys = True
            self.format_options = {
                'json': {
                    'format': True,
                    'indent': self.indent,
                    'sort_keys': self.sort_keys
                }
            }
            self.formatter = JSONFormatter(
                **self.kwargs,
                format_options=self.format_options
            )
            self.mime = 'text'

        def test_format_body_should_format_in_json(self):
            body = '{"key":"value"}'
            expected

# Generated at 2022-06-13 22:06:38.828065
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    fp = JSONFormatter()

# Generated at 2022-06-13 22:06:42.126710
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():

    # Test 1: Must return the same body when it's not JSON.

    formatter = JSONFormatter()

    response_body = "this is not JSON data."

    assert formatter.format_body(response_body, "text/plain") == response_body


if __name__ == "__main__":
    test_JSONFormatter_format_body()

# Generated at 2022-06-13 22:06:54.570948
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()
    # Test JSON
    body = '{"a": 10, "b": [1, 2, 3]}'
    mime = 'json'
    assert formatter.format_body(body, mime) == '''\
{
  "a": 10,
  "b": [
    1,
    2,
    3
  ]
}'''
    # Test Invalid JSON
    body = "Not a json"
    mime = 'json'
    assert formatter.format_body(body, mime) == "Not a json"
    # Test Other mime type
    body = "{'a': 10, 'b': [1, 2, 3]}"
    mime = 'javascript'

# Generated at 2022-06-13 22:06:58.244311
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    assert JSONFormatter(
        format_options={'json' : {
            'format': True,
            'indent': 4,
            'sort_keys': True}},
        explicit_json=True,
        output_options={'pretty': False, 'colors': True})

# Generated at 2022-06-13 22:07:10.268371
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    fp = JSONFormatter(format_options={
        'json': {'format': True, 'indent': 2, 'sort_keys': False}
    })
    b = '{"a": [1, 2], "b": 1234}'
    m = 'json'
    body = fp.format_body(b, m)
    assert body == '{\n  "a": [\n    1,\n    2\n  ],\n  "b": 1234\n}'
    b = '{"a": [1, 2], "b": 1234, "a": "123"}'
    m = 'json'
    body = fp.format_body(b, m)

# Generated at 2022-06-13 22:07:22.141959
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    class TestJSONFormatter(JSONFormatter):
        def __init__(self, **kwargs):
            kwargs = {
                'format_options': None,
                'explicit_json': True,
            }
            super().__init__(**kwargs)

    test_instance = TestJSONFormatter()

# Generated at 2022-06-13 22:07:57.775049
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    kwargs = {
        "explicit_json": False,
        "format_options": {
            "json": {
                "indent": 2,
                "format": True,
                "sort_keys": False
            }
        },
        "color_mode": "disabled"
    }

    formatter = JSONFormatter(**kwargs)

    # Invalid JSON
    body = '{a: 1, b: 2}'
    mime = 'text/javascript'
    assert formatter.format_body(body, mime) == body

    # Valid JSON
    body = '{"a": 1, "b": 2}'
    mime = 'text/javascript'
    assert formatter.format_body(body, mime) == '{\n  "a": 1,\n  "b": 2\n}'

# Generated at 2022-06-13 22:08:10.273397
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    import json
    from collections import OrderedDict
    from httpie.plugins import JSONFormatter

    test_json = [
        OrderedDict([('a',1), ('b',2)]),
        OrderedDict([('b',2), ('a',1)]),
        OrderedDict([('a',1), ('a',1)]),
    ]

    test_body = [json.dumps(obj) for obj in test_json]
    test_mime = ['json','text','json']
    test_kwargs = [{}, {'indent':0}, {'sort_keys':False}]


# Generated at 2022-06-13 22:08:20.667295
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(**{'explicit_json': False, 'format_options': {'json': {'format': True, 'sort_keys': True, 'indent': None}}})
    body = formatter.format_body('[{"name": "test"},{"name": "another test"}]', 'json')
    assert(body == '[\n    {\n        "name": "test"\n    },\n    {\n        "name": "another test"\n    }\n]')

    formatter = JSONFormatter(**{'explicit_json': False, 'format_options': {'json': {'format': False, 'sort_keys': True, 'indent': None}}})
    body = formatter.format_body('[{"name": "test"},{"name": "another test"}]', 'json')
   

# Generated at 2022-06-13 22:08:31.532908
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    format_options = {
        'json': {
            'format': True,
            'sort_keys': True,
            'indent': 2,
        }
    }
    kwargs = {
        'explicit_json': False,
        'format_options': format_options
    }
    formatter = JSONFormatter(**kwargs)

    headers = {
        'Content-Type': 'application/json'
    }
    body = '{"Hello": "World"}'
    actual = formatter.format_body(body, headers['Content-Type'])
    expected = '{\n  "Hello": "World"\n}'
    assert expected == actual

    headers = {
        'Content-Type': 'application/json'
    }
    body = '{"Hello": "World"}'
    actual = formatter

# Generated at 2022-06-13 22:08:43.281009
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(format_options={'json': {'format': True, 'indent': 2, 'sort_keys': False}})
    body = '{"key1": "value1", "key2": "value2"}'
    expected = '{\n  "key1": "value1",\n  "key2": "value2"\n}'
    assert formatter.format_body(body=body, mime='text/javascript') == expected
    body = '{"key1": "value1", "key2": "value2"}'
    expected = '{\n  "key1": "value1",\n  "key2": "value2"\n}'
    assert formatter.format_body(body=body, mime='text/json') == expected

# Generated at 2022-06-13 22:08:51.333606
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.plugins import FormatterPlugin

    test_format_options = {
        'json': {
            'format': True,
            'indent': 2,
            'sort_keys': False,
            'quote_keys': False,
        }
    }

    test_kwargs = {
        'explicit_json': True
    }

    formatter = FormatterPlugin(format_options=test_format_options, **test_kwargs)
    json_formatter = JSONFormatter(format_options=test_format_options, **test_kwargs)
    result = json_formatter.format_body(formatter)
    assert result == '{\n  "a": "b"\n}'

# Generated at 2022-06-13 22:08:56.264883
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter()
    object = {'name': 'Bjarne Stroustrup', 'occupation': 'computer science'}
    json_string = json.dumps(object)
    result = json_formatter.format_body(json_string, 'json')
    assert result == json_string

# Generated at 2022-06-13 22:09:04.781676
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(format_options={'json': {'format': 1, 'indent': 4, 'sort_keys': 0}}, kwargs={'explicit_json': 1})
    assert formatter.format_body('{"a": "xyz"}', 'json') == '{\n    "a": "xyz"\n}'
    assert formatter.format_body('abc', 'json') == 'abc'
    assert formatter.format_body(' "abc" ', 'javascript') == '{\n    "abc"\n}'

if __name__ == '__main__':
    test_JSONFormatter_format_body()

# Generated at 2022-06-13 22:09:14.326446
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    from httpie.plugins import FormatterPlugin
    from httpie.plugins.builtin import JSONPrettyFormatter
    from httpie.plugins.builtin import JSONFormatter
    from httpie.output.streams import BINARY_SUPPRESSED_NOTICE
    obj = JSONFormatter()
    assert isinstance(obj, FormatterPlugin)
    assert obj.format_name == 'json'
    assert obj.format_options == obj.__class__.format_options
    assert obj.format_options['json']['format']
    assert obj.format_options['json']['sort_keys']
    assert obj.format_options['json']['indent'] == 4


# Generated at 2022-06-13 22:09:21.803171
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    mime = 'application/json'
    body = '{"a":1}'
    args = [body, mime]
    kwargs = {
        'explicit_json': False,
        'format_options': {
            'json': {
                'format': True,
                'indent': 4,
                'sort_keys': True,
            }
        }
    }

    actual = JSONFormatter(**kwargs).format_body(*args)
    expected = '{\n    "a": 1\n}'

    assert actual == expected