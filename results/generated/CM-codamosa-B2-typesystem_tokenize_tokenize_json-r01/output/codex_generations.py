

# Generated at 2026-11-02 18:53:28.082574
# Unit test for constructor of class _TokenizingDecoder
def test__TokenizingDecoder():
    content = '{"a": 1}'
    decoder = _TokenizingDecoder(content=content)

    # scan_once should be set as a callable by the constructor
    assert callable(decoder.scan_once)

    # Decoding should produce a DictToken bound to the original content
    token = decoder.decode(content)
    assert isinstance(token, DictToken)
    assert token.string == content
    assert token.value == {"a": ScalarToken(1, 5, 6, content)}
    assert token.start == 0
    assert token.end == len(content) - 1

    # Extra JSONDecoder kwargs should still be forwarded to the superclass
    decoder2 = _TokenizingDecoder(strict=False, content=content)
    assert callable(decoder2.scan_once)
    assert decoder2.strict is False

    # content is a required keyword argument
    with pytest.raises(KeyError):
        _TokenizingDecoder()

# Generated at 2026-11-02 18:57:06.026229
# Unit test for function validate_json

# Generated at 2026-11-02 18:57:50.304240
# Unit test for function validate_json
def test_validate_json():from typesystem.fields import String
from typesystem.tokenize.json import validate_json


# Generated at 2026-11-02 19:00:35.445385
# Unit test for function tokenize_json