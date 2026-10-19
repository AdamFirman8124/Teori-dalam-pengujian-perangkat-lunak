

# Generated at 2022-06-13 22:01:54.984830
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    plugin = JSONFormatter(format_options={'json': {'format': True, 'indent': 4, 'sort_keys': True}})

    # test if invalid JSON is ignored
    body = plugin.format_body('{"test": invalid}', 'json')
    assert body == '{"test": invalid}'

    # JSON response with sort_keys and indent
    new_body = plugin.format_body('{"sample": "json", "test": "abc"}', 'json')
    assert new_body == '{\n    "sample": "json",\n    "test": "abc"\n}'

    # JSON response without sort_keys
    new_body = plugin.format_body('{"sample": "json", "test": "abc"}', 'json')

# Generated at 2022-06-13 22:02:00.283101
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    formatter = JSONFormatter(
        # Assert if format_options is not a dict
        format_options={},
        # Assert if kwargs is not a dict
        kwargs={}
    )
    assert formatter.enabled is False


# Generated at 2022-06-13 22:02:03.029218
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    foo = JSONFormatter(explicit_json=True)
    assert foo.format_body("{'foo1': 1}", "text") == '{"foo1": 1}'

# Generated at 2022-06-13 22:02:09.140774
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    options = {'options': {'json': {'format': True, 'indent': 2, 'sort_keys': False}}}
    print(JSONFormatter(**options).format_body('{"b": [1, 2], "a": 3}', 'application/json'))


# Generated at 2022-06-13 22:02:16.873373
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter()
    mime = "text"
    body = '{"a": 1, "b": 2}'
    json_formatter.kwargs['explicit_json'] = False
    """
    If explicit JSON is not specified and the mime type is not of a
    supported type then the body is not formatted and is returned as
    it is.
    """
    assert json_formatter.format_body(body, mime) == body

    # Reset for next unit test
    json_formatter.kwargs['explicit_json'] = False

    # Test when explicit JSO is specified
    json_formatter.kwargs['explicit_json'] = True
    """
    If explicit JSON is specified and mime type is not supported
    then the body is formatted.
    """
    formatted_body = json

# Generated at 2022-06-13 22:02:17.774660
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    pass



# Generated at 2022-06-13 22:02:27.267174
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter()
    string_json = "{'key1': 'value1', 'key2': 'value2'}"
    json_obj = json.dumps({
        "key1": "value1",
        "key2": "value2"
    })
    assert json_formatter.format_body(string_json, 'json') == json_obj
    assert json_formatter.format_body(string_json, 'not_json') == string_json
    assert json_formatter.format_body(json_obj, 'json') == json_obj

# Generated at 2022-06-13 22:02:30.246557
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    new_JSONFormatter = JSONFormatter()
    assert new_JSONFormatter.enabled is True

# Generated at 2022-06-13 22:02:39.621858
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Test class instanciation
    formatter = JSONFormatter(
        # 'kwargs' are incoming key word arguments
        kwargs = {
            'explicit_json' : True,
        },
        format_options = {
            'json' : {
                'sort_keys' : True,
                'indent' : 4,
            },
        },
    )
    # Test method format_body
    mime = 'application/json'
    json_str = '{"a": "b"}'
    assert formatter.format_body(json_str, mime) == json_str
    # Simulate keyword arguments for the method format_body of class JSONFormatter
    kw_args = {
        'body' : json_str,
        'mime' : mime,
    }
    # Execute the

# Generated at 2022-06-13 22:02:44.852937
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    sample_for_test = {
        'sample': [
            {
                'id': 'a',
                'value': 90
            },
            {
                'id': 'b',
                'value': 60
            }
        ]
    }

    sample_for_test_str = json.dumps(obj=sample_for_test)
    sort_keys = False
    indent = None
    expected = sample_for_test_str

    test_formatter = JSONFormatter(
        format_options={
            'json': {
                'format': True,
                'indent': indent,
                'sort_keys': sort_keys
            }
        },
        explicit_json=False
    )
    assert test_formatter.format_body(sample_for_test_str, 'json') == expected

# Generated at 2022-06-13 22:02:56.418567
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    body_json = '{"type": "http", "url": "http://httpie.org"}'
    body_not_json = 'haha'
    mime_json = 'json'
    mime_not_json = 'image/png'
    mime_text = 'text/plain'
    # Case when body is obviously JSON
    formatter = JSONFormatter(explicit_json=True)
    assert formatter.format_body(body_json, mime_json) == body_json
    assert formatter.format_body(body_not_json, mime_json) == body_not_json
    # Case when body is obviously not JSON
    formatter = JSONFormatter(explicit_json=False)
    assert formatter.format_body(body_json, mime_not_json) == body_json


# Generated at 2022-06-13 22:03:06.389488
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter()

    assert json_formatter.format_body('{"name": "value"}', 'json') == \
           '{\n    "name": "value"\n}'
    assert json_formatter.format_body('{"name": "value"}', 'javascript') == \
           '{\n    "name": "value"\n}'
    assert json_formatter.format_body('{"name": "value"}', 'text') == \
           '{\n    "name": "value"\n}'
    assert json_formatter.format_body('{"name": "value"}', 'html') == \
           '{"name": "value"}'

# Generated at 2022-06-13 22:03:16.013741
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():

    formatter = JSONFormatter()

    # Case 1
    # Input
    i_body = "{\"test\":\"json\"}"
    i_mime = "json"
    i_format_options = {'json': {'format': True, 'sort_keys': False, 'indent': 4}}
    i_kwargs = {'explicit_json': True}
    formatter.format_options = i_format_options
    formatter.kwargs = i_kwargs
    # Expect
    e_body = "{\"test\": \"json\"}"

    # Case 2
    # Input
    i_body = "{\"test\":\"string\"}"
    i_mime = "json"
    i_format_options = {'json': {'format': True, 'sort_keys': False, 'indent': 4}}
    i

# Generated at 2022-06-13 22:03:27.168658
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    body_str = '{"a": 123, "b": "xyz"}'
    mime = 'json'
    format_options = {
        'json': {
            'format': True,
            'indent': 2,
            'sort_keys': True,
        }
    }

    formatter = JSONFormatter(format_options=format_options)
    assert formatter.format_body(body=body_str, mime=mime) == '{\n  "a": 123,\n  "b": "xyz"\n}'

    format_options['json']['format'] = False
    formatter = JSONFormatter(format_options=format_options)
    assert formatter.format_body(body=body_str, mime=mime) == body_str


# Generated at 2022-06-13 22:03:35.739958
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.plugins.builtin import FormatterPlugin
    import json

    class JSONFormatter(FormatterPlugin):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.enabled = self.format_options['json']['format']

        def format_body(self, body: str, mime: str) -> str:
            maybe_json = [
                'json',
                'javascript',
                'text',
            ]
            if (self.kwargs['explicit_json']
                    or any(token in mime for token in maybe_json)):
                try:
                    obj = json.loads(body)
                except ValueError:
                    pass  # Invalid JSON, ignore.

# Generated at 2022-06-13 22:03:44.617231
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    def test_JSONFormatter_format_body_non_json():
        formatter = JSONFormatter(format_options={'json': {'format': True}})
        body = formatter.format_body('{"test": "Hello world"}', 'csv')
        assert body == '{"test": "Hello world"}'

    test_JSONFormatter_format_body_non_json()

    def test_JSONFormatter_format_body_json():
        formatter = JSONFormatter(format_options={'json': {'format': True}})
        body = formatter.format_body('{"test": "Hello world"}', 'json')
        assert body == '{\n    "test": "Hello world"\n}'

    test_JSONFormatter_format_body_json()

# Generated at 2022-06-13 22:03:51.574181
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    jsonFormatter = JSONFormatter(format_options=1, kwargs=2)
    assert isinstance(jsonFormatter, JSONFormatter)
    assert jsonFormatter.format_options == 1
    assert jsonFormatter.kwargs == 2
    assert jsonFormatter.enabled == False
    assert jsonFormatter.name == 'json'

# Generated at 2022-06-13 22:04:02.302487
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(format_options={"json": {'format': True, 'indent': 3, 'sort_keys': True}})
    body = '{"key": "value"}'
    formatted_body = formatter.format_body(body=body, mime='application/json')
    assert formatted_body == '''{
   "key": "value"
}'''

    body = '{"key": "value"}'
    formatted_body = formatter.format_body(body=body, mime='text/plain')
    assert formatted_body == '''{
   "key": "value"
}'''

    body = '{"key": "value"}'
    formatted_body = formatter.format_body(body=body, mime='text/html')
    assert formatted_body == body

    # Test

# Generated at 2022-06-13 22:04:09.066930
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    formatteroptions = {
        'json': {
            'format': True,
            'indent': 2,
            'sort_keys': False
        }
    }
    assert(JSONFormatter(formatter_options=formatteroptions, **{}).enabled)
    assert not(JSONFormatter(**{}).enabled)


# Generated at 2022-06-13 22:04:19.028271
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    """
    test method format_body of class JSONFormatter
    this is a test for the bug reported at
    https://bugzilla.redhat.com/show_bug.cgi?id=1622640
    """
    import logging

    logging.basicConfig(level=logging.DEBUG)
    formatter = JSONFormatter(
        format_options={"json": {"format": True, "indent": 2}})

# Generated at 2022-06-13 22:04:31.775743
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter(**{'python_input_json': ''})
    input = '{"id":1}'
    output = '{"id": 1}'
    mime = 'text/json'
    assert json_formatter.format_body(input, mime) == output

# Generated at 2022-06-13 22:04:34.273973
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    assert JSONFormatter(format_options={"json":{"indent":4, "sort_keys": True, "format":True}})

# Generated at 2022-06-13 22:04:40.059935
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    # Arrange
    formatter_options = {
        'json': {
            'format': True,
            'indent': 1,
            'sort_keys': True
        }
    }
    formatter = JSONFormatter(format_options=formatter_options, explicit_json=False)
    assert formatter.format_options == formatter_options
    assert formatter.enabled == True


# Generated at 2022-06-13 22:04:49.317898
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    assert '{"foo": 42}' == JSONFormatter().format_body('{"foo": 42}', '')
    assert '{"foo": [42]}' == JSONFormatter().format_body('{"foo": [42]}', '')
    assert '{"foo": [42]}' == JSONFormatter(explicit_json=True).format_body('{"foo": [42]}', '')
    assert '{"foo": [42]}' == JSONFormatter().format_body('{"foo": [42]}', 'json')
    assert '{"foo": [42]}' == JSONFormatter().format_body('{"foo": [42]}', 'javascript')
    assert '{"bar": 42}' == JSONFormatter(explicit_json=True).format_body('{"bar": 42}', 'json')
    assert '{"foo": [42]}' == JSON

# Generated at 2022-06-13 22:04:57.561040
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
	import pytest
	from httpie.plugins import FormatterPlugin
	jsonFormatter =JSONFormatter(format_options={'json':{'format':'True', 'indent':4, 'sort_keys':'True'}})
	assert jsonFormatter.format_options['json']['format'] == 'True'
	assert jsonFormatter.format_options['json']['indent'] == 4
	assert jsonFormatter.format_options['json']['sort_keys'] == 'True'


# Generated at 2022-06-13 22:05:11.741546
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    """
    Arguments:
    body: raw body data which is to be formatted
    mime: mime type of body data
    """
    body = '[{"key": "value"}]'
    mime = 'application/json'
    assert JSONFormatter.format_body(body, mime) == '[\n  {\n    "key": "value"\n  }\n]'
    mime = 'application/javascript'
    assert JSONFormatter.format_body(body, mime) == '[\n  {\n    "key": "value"\n  }\n]'
    mime = 'text/plain'
    assert JSONFormatter.format_body(body, mime) == '[\n  {\n    "key": "value"\n  }\n]'
    mime = 'text/html'

# Generated at 2022-06-13 22:05:17.957251
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    body = '{"id":1}'
    mime = 'application/json'
    kwargs = {
        'explicit_json':False,
        'format_options': {
            'json': {
                'format':True,
                'sort_keys':True,
                'indent':2
            }
        },
    }
    instance = JSONFormatter(**kwargs)
    assert instance.format_body(body, mime) == '{\n  "id": 1\n}'

# Generated at 2022-06-13 22:05:19.522150
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    formatter = JSONFormatter()
    assert formatter.enabled == True


# Generated at 2022-06-13 22:05:26.728744
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    formatter = JSONFormatter(
        format_options={'json': {'format': True, 'indent': 4, 'sort_keys': True}},
        explicit_json=False
    )
    assert formatter.format_options == {'json': {'format': True, 'indent': 4, 'sort_keys': True}}
    assert formatter.explicit_json == False


# Generated at 2022-06-13 22:05:29.914192
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter({'sort_keys': True, 'indent': 4})
    assert formatter.format_body('{"a": 1}', 'json') == '{\n    "a": 1\n}'