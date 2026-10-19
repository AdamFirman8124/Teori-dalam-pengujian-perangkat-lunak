

# Generated at 2022-06-13 22:01:52.549875
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    formatter = JSONFormatter(json={'format': False, 'indent': 0, 'sort_keys': True},
                              headers={'headers': True, 'host': True, 'auth': True},
                              style={'style': 'solarized', 'colors': True, 'force_styling': True})
    assert formatter.enabled == False



# Generated at 2022-06-13 22:02:02.880582
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    options = {
        'json': {
            'format': True,
            'indent': 4,
            'sort_keys': True
        }
    }
    body = '{"nombre":"paco","edad":30,"email":"paco@gmail.com","id":1}'
    expected = '''{
    "edad": 30,
    "email": "paco@gmail.com",
    "id": 1,
    "nombre": "paco"
}'''
    formatter = JSONFormatter(format_options=options)
    assert formatter.format_body(body, "json") == expected



# Generated at 2022-06-13 22:02:06.544774
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    json_formatter = JSONFormatter(format_options={'json': {'format': True}})
    assert json_formatter.enabled


# Generated at 2022-06-13 22:02:20.175177
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    kwargs = {
                'explicit_json': False,
                'format_options': {
                    'json': {
                        'format': False,
                        'indent': 2,
                        'sort_keys': True
                    }
                }
            }
    json_formatter = JSONFormatter(**kwargs)

    body = "{\"foo\":[\"bar\", \"baz\"]}"
    mime = "bad_mime"

    assert json_formatter.format_body(body, mime) == body

    body = "{\"foo\":[\"bar\", \"baz\"]}"
    mime = "json"

    assert json_formatter.format_body(body, mime) == body

    body = "{\"foo\":[\"bar\", \"baz\"]}"
    mime = "text"


# Generated at 2022-06-13 22:02:31.333360
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():

    plugin = JSONFormatter(format_options={'json' : {'format': True, 'indent': 4, 'sort_keys': True}})
    response_body = json.dumps({'foo': 42, 'bar': {'in': 'one', 'out': 'two'}})
    response_mime = 'json'
    assert plugin.format_body(body=response_body, mime=response_mime) == json.dumps(
        obj={'foo': 42, 'bar': {'in': 'one', 'out': 'two'}},
        sort_keys=True,
        ensure_ascii=False,
        indent=4
    )

    response_body = json.dumps({'foo': 42, 'bar': {'in': 'one', 'out': 'two'}})
    response_

# Generated at 2022-06-13 22:02:42.523104
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    assert(JSONFormatter().format_body(
    "[[\"Item1\", 1], [\"Item2\", 2], [\"Item3\", 3], [\"Item4\", 4]]",
    "json") == '''
[
    [
        "Item1",
        1
    ],
    [
        "Item2",
        2
    ],
    [
        "Item3",
        3
    ],
    [
        "Item4",
        4
    ]
]
''')

# Generated at 2022-06-13 22:02:54.408925
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from test_utils import MockData, MockArguments
    arguments = MockArguments()
    data = MockData()
    formatter = JSONFormatter(format_options=arguments.format_options,
                              explicit_json=True)
    # Body is valid json
    expected = '{\n    "foo": "bar"\n}'
    result = formatter.format_body(body='{"foo": "bar"}',
                                   mime='application/json')
    assert result == expected
    # Body is not valid JSON
    expected = '<xml>bar</xml>'
    result = formatter.format_body(body=expected,
                                   mime='application/xml')
    assert result == expected
    # Body is valid JSON but key sorting is disabled
    expected = '{\n    "foo": "bar"\n}'

# Generated at 2022-06-13 22:03:06.520227
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    from httpie.plugins import builtin
    from httpie.compat import str

    httpie = builtin.HTTPie()
    Object = JSONFormatter(httpie, {'json': {'format': True}})

    # json
    assert Object.format_body('{"a": "b", "c": "d"}', 'json') == '{\n    "a": "b",\n    "c": "d"\n}'
    assert Object.format_body('{"a": "b", "c": "d"}', 'json') == '{\n    "a": "b",\n    "c": "d"\n}'

    # failure
    assert Object.format_body('{"a": "b", "c": "d', 'json') == '{"a": "b", "c": "d'

# Generated at 2022-06-13 22:03:09.365830
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    JSONFormatter.__bases__ = (object,)
    # Create an instance of the class.
    json_formatter = JSONFormatter()
    # Call the method.
    assert json_formatter.fo

# Generated at 2022-06-13 22:03:21.454118
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    '''
    Test the method format_body in the class JSONFormatter
    '''

    # When we have a valid json
    # Given
    formatter = JSONFormatter()
    formatter.kwargs = {'explicit_json': False}
    formatter.format_options = {
        'json': {
            'format': True,
            'indent': 4,
            'sort_keys': False},
    }