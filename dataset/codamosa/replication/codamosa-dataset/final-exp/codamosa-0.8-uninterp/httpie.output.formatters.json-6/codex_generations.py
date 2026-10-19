

# Generated at 2022-06-13 22:01:51.971299
# Unit test for method format_body of class JSONFormatter

# Generated at 2022-06-13 22:02:04.251956
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Test JSON output
    from httpie.formatters.json import JSONFormatter
    obj = {
        'a': 'b',
        'c': 1,
    }
    # Formatter does not format JSON
    assert JSONFormatter(format_options=dict(json=dict(format=False))).format_body(body=json.dumps(obj),mime='application/json') == json.dumps(obj)
    # Formatter formats JSON
    assert JSONFormatter(format_options=dict(json=dict(format=True))).format_body(body=json.dumps(obj),mime='application/json') == json.dumps(obj, sort_keys=False, ensure_ascii=False, indent=None)

    # Test non-JSON output

# Generated at 2022-06-13 22:02:12.092830
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    assert JSONFormatter(**{'explicit_json': True, 'format_options': {'json':{'format': True, 'indent': 2, 'sort_keys': True}}}).format_body('{"a":1, "b":2}', 'json') == '{\n  "a": 1,\n  "b": 2\n}'
    assert JSONFormatter(**{'explicit_json': True, 'format_options': {'json':{'format': True, 'indent': 2, 'sort_keys': True}}}).format_body('{"a":1, "b":2}', 'javascript') == '{\n  "a": 1,\n  "b": 2\n}'

# Generated at 2022-06-13 22:02:17.500673
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(format_options={'json': {'indent': None, 'sort_keys': False, 'format': True}}, kwargs={'explicit_json': False})
    assert formatter.format_body('{"data": "value"}', 'json') == '{\n    "data": "value"\n}'

# Generated at 2022-06-13 22:02:29.940946
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    tester = JSONFormatter(format_options = {'json': {'format': False, 'indent': 2, 'sort_keys': True}},
                           explicit_json = False,
                           colors = None,
                           styles = None)
    body = '{"a": 5, "c": "hello", "b": 10}'
    mime = 'json'
    assert tester.format_body(body, mime) == ('{\n'
                                              '  "a": 5,\n'
                                              '  "b": 10,\n'
                                              '  "c": "hello"\n'
                                              '}')

    tester.format_options['json']['format'] = True

# Generated at 2022-06-13 22:02:39.462969
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    assert "" == JSONFormatter(format_options={"json": {"format": 0}}).format_body("", "")
    assert "" == JSONFormatter(format_options={"json": {"format": 1}}).format_body("", "")
    assert "" == JSONFormatter(format_options={"json": {"format": 1}}, kwargs={"explicit_json": 0}).format_body("", "")

    assert "1" == JSONFormatter(format_options={"json": {"format": 0}}, kwargs={"explicit_json": 1}).format_body("1", "")
    assert "1" == JSONFormatter(format_options={"json": {"format": 1}}, kwargs={"explicit_json": 1}).format_body("1", "")
    assert "1" == JSONFormatter

# Generated at 2022-06-13 22:02:49.770692
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(
        format_options={
            'json': {
                'format': False,
                'indent': 4,
                'sort_keys': True
            }
        },
        explicit_json=False,
    )

    # JSON
    assert formatter.format_body("""
    {
        "test": "json"
    }
    """, 'json') == """{
    "test": "json"
}"""

    # JSON with Unicode codepoints
    assert formatter.format_body("""
    {
        "test": "💩"
    }
    """, 'json') == """{
    "test": "💩"
}"""

    # JavaScript

# Generated at 2022-06-13 22:02:57.505181
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():

    # Example 1:
    # - body: {id: 10, name: "Foo"}
    # - format: True
    # - sort_keys: False
    # - indent: 2
    # - explicit_json: True
    # - mime:  application/json
    # Expect output:
    # {
    #   "id": 10,
    #   "name": "Foo"
    # }

    json_formatter_example1 = JSONFormatter(
        format_options={
            "json": {
                "format": True,
                "sort_keys": False,
                "indent": 2,
            }
        },
        explicit_json=True,
    )

    input_body = '{\"id\": 10, \"name\": \"Foo\"}'
    mime = 'application/json'


# Generated at 2022-06-13 22:03:00.390988
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    fmt = JSONFormatter()
    res = fmt.format_body('{"json":"value"}', 'json')
    assert res == '{\n    "json": "value"\n}'

# Generated at 2022-06-13 22:03:09.988070
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter()
    assert formatter.format_body('{"a": 1, "b": 2}', 'json') == '{\n    "a": 1, \n    "b": 2\n}'
    assert formatter.format_body('{"a": 1, "b": 2}', 'text') == '{\n    "a": 1, \n    "b": 2\n}'
    assert formatter.format_body('{"a": 1, "b": 2}', 'javascript') == '{\n    "a": 1, \n    "b": 2\n}'
    assert formatter.format_body('{"a": 1, "b": 2}', 'html') == '{"a": 1, "b": 2}'
