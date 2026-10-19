

# Generated at 2022-06-13 22:01:53.098464
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    from httpie.plugins import JSONFormatter
    formatterOptions = {'json': {'format': 'json', 'indent': 2, 'sort_keys': True}}
    formatter = JSONFormatter(**formatterOptions)
    assert type(formatter).__name__ == 'JSONFormatter'
    assert formatter.format_options['json']['format'] == 'json'
    assert formatter.format_options['json']['indent'] == 2
    assert formatter.format_options['json']['sort_keys'] == True


# Generated at 2022-06-13 22:02:00.287230
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json = JSONFormatter()
    print(json.format_body("{\"id\": 1, \"name\": \"A green door\", \"price\": 12.5, \"tags\": [\"home\", \"green\"]}", "json"))
    print(json.format_body("{\"id\": 1, \"name\": \"A green door\", \"price\": 12.5, \"tags\": [\"home\", \"green\"]}", "text"))

# Generated at 2022-06-13 22:02:11.343517
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # test with valid json string and with various mime types
    jf = JSONFormatter(kwargs={}, format_options={'json': {'format': True, 'indent': 4, 'sort_keys': False}})
    body = '{"body": "in json"}'
    formatted = jf.format_body(body, 'application/json')
    assert body == formatted, "MimeType: application/json"

    formatted = jf.format_body(body, 'json')
    assert body == formatted, "MimeType: json"

    formatted = jf.format_body(body, 'text/plain')
    assert body == formatted, "MimeType: text/plain"

    formatted = jf.format_body(body, 'text')
    assert body == formatted, "MimeType: text"

    formatted = j

# Generated at 2022-06-13 22:02:19.147411
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    import json
    body = "{ 'x':1, 'y':2 }"
    body_expected = '{"x": 1, "y": 2}'
    mime = "text"
    formatter = JSONFormatter()
    formatter.kwargs['explicit_json'] = False
    formatter.format_options['json']['sort_keys'] = True
    formatter.format_options['json']['indent'] = 4
    body_actual = formatter.format_body(body, mime)
    assert body_expected == body_actual

# Generated at 2022-06-13 22:02:24.677864
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter()
    assert json_formatter.format_body("{\"un\":\"nom\",\"deux\":\"choses\"}", "json") == \
        '{\n    "deux": "choses", \n    "un": "nom"\n}'

# Generated at 2022-06-13 22:02:37.216565
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()
    body = '{"test": "text"}'
    formatted_body = formatter.format_body(body, 'json')
    assert(formatted_body == '{\n    "test": "text"\n}')
    body = '{"test": "text"}'
    formatted_body = formatter.format_body(body, 'javascript')
    assert(formatted_body == '{\n    "test": "text"\n}')
    body = '{"test": "text"}'
    formatted_body = formatter.format_body(body, 'text')
    assert(formatted_body == '{\n    "test": "text"\n}')
    body = '{"test": "text"}'
    formatted_body = formatter.format_body(body, 'unknown')
   

# Generated at 2022-06-13 22:02:44.733592
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    assert JSONFormatter(format_options = {'json': {'format': True, 'indent': 4, 'sort_keys': True}}).format_body("""{
        "a": 1,
        "b": 2
    }""", 'json') == """{
    "a": 1,
    "b": 2
}"""


# Generated at 2022-06-13 22:02:52.536903
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter(explicit_json=False, format_options={'json': {'format': True, 'indent': 4, 'sort_keys': False}})
    mime = 'text/json'
    body = '{"test": "1", "test2": "2"}'
    expected_result = '{\n    "test": "1",\n    "test2": "2"\n}'
    result = json_formatter.format_body(body, mime)
    assert expected_result == result

# Generated at 2022-06-13 22:02:55.552627
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter(): 
    a = JSONFormatter()
    assert a.enabled == True

# Generated at 2022-06-13 22:03:05.779306
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():

    params = {
        'json': {
            'format': True,
            'sort_keys': False,
            'indent': 4,
        }
    }
    http_plugin = JSONFormatter(params=params, kwargs={'explicit_json': False})
    assert (http_plugin.format_body(
            '{"foo": {"bar": ["baz", null, 1.0, 2]}}', 'application/json'
    ) == '{\n    "foo": {\n        "bar": [\n            "baz",\n            null'
            ',\n            1.0,\n            2\n        ]\n    }\n}')

# Generated at 2022-06-13 22:03:22.627850
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    fp = JSONFormatter(kwargs={'explicit_json': True})
    assert fp.format_body('{"name": "justin", "age": 30}', '') == \
        '{\n    "age": 30,\n    "name": "justin"\n}'
    assert fp.format_body('{"name": "justin", "age": 30}',
                          'application/json') == \
        '{\n    "age": 30,\n    "name": "justin"\n}'
    assert fp.format_body('{"name": "justin", "age": 30}',
                          'application/javascript') == \
        '{\n    "age": 30,\n    "name": "justin"\n}'

# Generated at 2022-06-13 22:03:35.853375
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    uut = JSONFormatter(format_options = {'json': {'format': True, 'sort_keys': False, 'indent': 4}})
    json_dict = {'a': 1, 'b': 2, 'c': 'texto'}
    json_string = json.dumps(obj=json_dict, sort_keys=False, ensure_ascii=False, indent=4)
    ret = uut.format_body(body=json.dumps(json_dict), mime='json')
    assert json_string == ret
    assert json_string == uut.format_body(body=json.dumps(json_dict), mime='application/json')
    assert json_string == uut.format_body(body=json.dumps(json_dict), mime='text/json')

# Generated at 2022-06-13 22:03:44.943813
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    plugin = JSONFormatter()
    # Test for valid JSON
    json_input = '{"a": "A"}'
    assert plugin.format_body(json_input, 'application/json') == json_input
    # Test for invalid JSON
    json_input = '{"a": "A"}_'
    assert not plugin.format_body(json_input, 'application/json') == json_input
    # Test for valid JSON with no mimetype
    json_input = '{"a": "A"}'
    assert plugin.format_body(json_input, 'text/plain') == json_input
    # Test for valid JSON with javascript mimetype
    json_input = '{"a": "A"}'
    assert plugin.format_body(json_input, 'application/javascript') == json_input

# Generated at 2022-06-13 22:03:52.675539
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter()
    body_to_test = '{"a": "b"}' + "\n" + '{"c": "d"}'
    mime_to_test = 'json'
    body_formatted = json_formatter.format_body(body=body_to_test, mime=mime_to_test)
    assert body_formatted == '{\n    "a": "b",\n    "c": "d"\n}\n'


# Generated at 2022-06-13 22:03:56.435345
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    assert (JSONFormatter(
        verbose=1,
        colors=256,
        json={
            'format': True,
            'sort_keys': False,
            'indent': 2
        }
    ).format_options['json']['format'] == True)


# Generated at 2022-06-13 22:03:59.085417
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()
    assert formatter.format_body(body, 'json') == body
    assert formatter.format_body(body, 'javascript') == body
    assert formatter.format_body(body, 'text') == body

# Generated at 2022-06-13 22:04:03.633547
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter()
    assert json_formatter.format_body(
        '{"foo": "bar"}',
        'application/json'
    ) == '{\n    "foo": "bar"\n}'



# Generated at 2022-06-13 22:04:12.303453
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Given
    body = '{"test": "abc"}'
    mime = 'json'
    explicit_json = True
    format_options = {
        "json": {
            "format": True,
            "indent": 2,
            "sort_keys": True
        }
    }
    kwargs = {
        "explicit_json": explicit_json,
        "format_options": format_options
    }
    formatter = JSONFormatter(**kwargs)

    # When
    result = formatter.format_body(body, mime)

    # Then
    assert result == '{\n  "test": "abc"\n}'


# Generated at 2022-06-13 22:04:26.177206
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(explicit_json=False, headers = None)

    def test_format_body(body, mime):
        assert formatter.format_body(body, mime) == body

    test_format_body(body='{}', mime='json')
    test_format_body(body='{}', mime='application/json')
    test_format_body(body='{}', mime='application/javascript')
    test_format_body(body='{}', mime='text/javascript')
    test_format_body(body='{}', mime='text/html')
    test_format_body(body='{', mime='json')
    test_format_body(body='{', mime='application/json')

# Generated at 2022-06-13 22:04:30.168522
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    test_JSONFormatter = JSONFormatter(explicit_json=True,format_options='json')
    assert test_JSONFormatter.__init__() == None
