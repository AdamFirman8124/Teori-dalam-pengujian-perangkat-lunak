

# Generated at 2026-11-03 01:37:35.101430
# Unit test for function validate_yaml

# Generated at 2026-11-03 01:40:17.516090
# Unit test for function validate_yaml

# Generated at 2026-11-03 01:43:35.456886
# Unit test for function validate_yaml
def test_validate_yaml():
    class Book(Schema):
        title: str
        author: str

    content = "title: Frankenstein\nauthor: Mary Shelley"
    value, error = module_0.validate_yaml(content, validator=Book)
    assert value == {"title": "Frankenstein", "author": "Mary Shelley"}
    assert error is None