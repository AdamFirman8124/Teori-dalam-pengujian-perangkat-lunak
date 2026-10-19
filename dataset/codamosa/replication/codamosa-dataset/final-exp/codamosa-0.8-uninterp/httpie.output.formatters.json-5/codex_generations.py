

# Generated at 2022-06-13 22:01:49.671129
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    assert JSONFormatter(format_options={'json': {'indent': 0, 'sort_keys': False}}).format_body('{}', 'application/json') == '{}'


# Generated at 2022-06-13 22:02:03.452387
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    formatter = JSONFormatter(format_options={
        'json': {
            'format': True,
            'sort_keys': True,
            'indent': 2
        }}
    )
    obj = dict(d=dict(a=0, b=1), a=0, b=1)
    obj_json = json.dumps(obj, sort_keys=True)
    # JSON
    assert formatter.format_body(obj_json, 'json') == obj_json
    # Slightly broken JSON
    assert formatter.format_body('{"a": 1, "b": 2}', 'json') == '{"a": 1, "b": 2}'
    # Invalid JSON

# Generated at 2022-06-13 22:02:11.675136
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    assert JSONFormatter().format_body(
        '{"foo": 1, "bar": 2}',
        ''
    ) == '{\n    "bar": 2,\n    "foo": 1\n}'
    assert JSONFormatter().format_body(
        '{"foo": 1, "bar": 2}',
        'application/json'
    ) == '{\n    "bar": 2,\n    "foo": 1\n}'
    assert JSONFormatter().format_body(
        '{"foo": 1, "bar": 2}',
        'text/plain'
    ) == '{\n    "bar": 2,\n    "foo": 1\n}'

# Generated at 2022-06-13 22:02:21.887904
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    tester = JSONFormatter(**{
        'format_options': {
            'json': {
                'format': True,
                'sort_keys': True,
                'indent': 4
            },
            'colors': False
        },
        'explicit_json': True
    })
    assert tester.format_body('{"foo":"bar"}', 'application/json') == (
        '{\n'
        '    "foo": "bar"\n'
        '}'
    )
    assert tester.format_body('{}', 'application/json') == '{\n}'
    assert tester.format_body('{"foo":"bar"}', 'text/html') == '{\n    "foo": "bar"\n}'

# Generated at 2022-06-13 22:02:32.517905
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    body = '{"a": "b"}'
    json_formatter = JSONFormatter(format=True)
    assert json_formatter.format_body(body=body, mime='application/json') == '{\n    "a": "b"\n}'

    body = '{  "a":  "b" }'
    json_formatter = JSONFormatter(format=True)
    assert json_formatter.format_body(body=body, mime='application/json') == '{\n    "a": "b"\n}'

    body = json.dumps(obj={'a': 'b'}, sort_keys=True, ensure_ascii=False, indent=2)
    json_formatter = JSONFormatter(format=True)

# Generated at 2022-06-13 22:02:43.406960
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    body = '{"b": 2, "a": 1}'
    assert JSONFormatter(json={'format': True, 'indent': None, 'sort_keys': True}).format_body(body, 'application/json') == '{\n    "a": 1,\n    "b": 2\n}'
    assert JSONFormatter(json={'format': True, 'indent': 4, 'sort_keys': True}).format_body(body, 'application/json') == '{\n    "a": 1,\n    "b": 2\n}'
    assert JSONFormatter(json={'format': True, 'indent': None, 'sort_keys': False}).format_body(body, 'application/json') == '{\n    "b": 2,\n    "a": 1\n}'
    assert JSON

# Generated at 2022-06-13 22:02:55.007883
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    json_formatter = JSONFormatter(explicit_json=False)

    json_formatter.kwargs['explicit_json'] = False
    assert json_formatter.format_body(
        body='{"a": 1, "b": 2}',
        mime='json'
    ) == '{\n    "a": 1,\n    "b": 2\n}'
    assert json_formatter.format_body(
        body='[1,2,3]',
        mime='json'
    ) == '[\n    1,\n    2,\n    3\n]'

    json_formatter.kwargs['explicit_json'] = True
    assert json_formatter.format_body(
        body='{"a": 1, "b": 2}',
        mime='xml'
    )

# Generated at 2022-06-13 22:03:04.620095
# Unit test for constructor of class JSONFormatter
def test_JSONFormatter():
    jf = JSONFormatter(
        format_options={
            'json': {
                'format': True,
                'indent': 4,
                'sort_keys': True
            }
        },
        explicit_json=False
    )
    assert jf.enabled is True
    assert jf.kwargs['explicit_json'] is False
    assert jf.format_options['json']['format'] is True
    assert jf.format_options['json']['indent'] is 4
    assert jf.format_options['json']['sort_keys'] is True



# Generated at 2022-06-13 22:03:15.297974
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    # Case 1: JSON body is correctly indented
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

# Generated at 2022-06-13 22:03:23.991850
# Unit test for method format_body of class JSONFormatter
def test_JSONFormatter_format_body():
    c = JSONFormatter()
    assert c.format_body(
        body=b'{"key": "value"}',
        mime='json'
    ) == '{\n    "key": "value"\n}'
    assert c.format_body(
        body=b'{"key": "value"}',
        mime='application/json'
    ) == '{\n    "key": "value"\n}'
    assert c.format_body(
        body=b'{"key": "value"}',
        mime='text'
    ) == '{\n    "key": "value"\n}'
    assert c.format_body(
        body=b'{"key": "value"}',
        mime='application/javascript'
    ) == '{\n    "key": "value"\n}'