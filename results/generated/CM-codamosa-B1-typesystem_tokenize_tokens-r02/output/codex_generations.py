

# Generated at 2026-10-24 11:28:54.824050
# Unit test for constructor of class Token

# Generated at 2026-10-24 11:28:57.239293
# Unit test for constructor of class Token

# Generated at 2026-10-24 11:28:59.659490
# Unit test for constructor of class Token

# Generated at 2026-10-24 11:29:02.094116
# Unit test for constructor of class ScalarToken

# Generated at 2026-10-24 11:29:04.494051
# Unit test for constructor of class ScalarToken

# Generated at 2026-10-24 11:29:06.914356
# Unit test for constructor of class ScalarToken

# Generated at 2026-10-24 11:29:09.331945
# Unit test for method __hash__ of class ScalarToken

# Generated at 2026-10-24 11:29:24.283714
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():from typesystem.tokens import ScalarToken


# Generated at 2026-10-24 11:29:30.537772
# Unit test for constructor of class Token
def test_Token():
    value = {"key": "value"}
    token = Token(value, start_index=2, end_index=5, content="0123456789")

    assert token._value is value
    assert token._start_index == 2
    assert token._end_index == 5
    assert token._content == "0123456789"
    assert token.string == "2345"

# Generated at 2026-10-24 11:29:31.852333
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Same value + same start/end indices -> equal
    assert ScalarToken("abc", 0, 2, "abc") == ScalarToken("abc", 0, 2, "abc")

    # Content is NOT part of equality
    assert ScalarToken(1, 0, 0, "1") == ScalarToken(1, 0, 0, "different content")

    # Same value, different start index -> not equal
    assert not (ScalarToken("abc", 0, 2, "abc") == ScalarToken("abc", 1, 3, "abc"))

    # Same value, different end index -> not equal
    assert not (ScalarToken("abc", 0, 2, "abc") == ScalarToken("abc", 0, 1, "abc"))

    # Different value, same indices -> not equal
    assert not (ScalarToken("abc", 0, 2, "abc") == ScalarToken("abd", 0, 2, "abd"))

    # Non-Token operands -> not equal (isinstance guard)
    assert not (ScalarToken("abc", 0, 2, "abc") == "abc")
    assert not (ScalarToken("abc", 0, 2, "abc") == None)  # noqa: E711
    assert not (ScalarToken("abc", 0, 2, "abc") == 42)

    # __ne__ is derived from __eq__
    assert ScalarToken("abc", 0, 2, "abc") != ScalarToken("abc", 1, 3, "abc")

    # Subclasses compare structurally via _get_value()
    content = '{"k": 1}'
    dict_a = DictToken(
        {ScalarToken("k", 1, 3, content): ScalarToken(1, 5, 5, content)}, 0, 6, content
    )
    dict_b = DictToken(
        {ScalarToken("k", 1, 3, content): ScalarToken(1, 5, 5, content)}, 0, 6, content
    )
    assert dict_a == dict_b
    assert not (dict_a == DictToken({ScalarToken("k", 1, 3, content): ScalarToken(2, 5, 5, content)}, 0, 6, content))

    list_a = ListToken([ScalarToken(1, 1, 1, "[1]")], 0, 2, "[1]")
    list_b = ListToken([ScalarToken(1, 1, 1, "[1]")], 0, 2, "[1]")
    assert list_a == list_b

    # Different container shapes with different values -> not equal

# Generated at 2026-10-24 11:29:33.161327
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:29:34.556766
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:29:35.870019
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:29:37.285573
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:29:38.620474
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:29:39.938401
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:29:41.265012
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:29:42.575530
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:29:43.904070
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:29:46.412485
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:29:49.017210
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:29:51.436426
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:29:53.943799
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:29:56.360126
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:29:58.777651
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:01.195116
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:03.609674
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:06.029155
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:08.441825
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:10.860821
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:13.278088
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:15.694308
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:18.111357
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:20.531123
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:22.948593
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:25.366954
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:27.788312
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:30.206215
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:32.624637
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:35.043793
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:37.459806
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:39.878139
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:42.295668
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:44.713660
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:47.130936
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:49.547860
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:51.970443
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:54.386450
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:56.802925
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:30:59.219710
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:31:01.635060
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:31:04.054277
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:31:07.034141
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:31:09.447428
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:31:11.863221
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:31:14.281458
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:31:19.480090
# Unit test for constructor of class DictToken
def test_DictToken():key_token = ScalarToken("name", 1, 6, '"name": "Alice"')

# Generated at 2026-10-24 11:31:21.122774
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:22.757351
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:24.081262
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:25.396384
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:26.852599
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:28.179359
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:29.494941
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:30.805835
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:33.386161
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:34.711671
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:36.024426
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:37.340102
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:38.657455
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:40.268709
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:41.579585
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:42.890863
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:44.215514
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:45.524654
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:31:52.613963
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:31:55.030580
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:31:57.446638
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:31:59.864688
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:02.446874
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:04.862976
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:07.280561
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:09.697869
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:12.113376
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:14.532482
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:16.951018
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:19.367586
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:21.783712
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:24.200811
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:26.621798
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:29.040322
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:31.459321
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:33.874791
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:36.290980
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:38.712030
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:41.128412
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:43.545398
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:45.963380
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:48.378695
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:50.795045
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:32:58.196409
# Unit test for constructor of class DictToken
def test_DictToken():key_token = ScalarToken("a", 1, 1, '{"a": 1}')

# Generated at 2026-10-24 11:32:59.525607
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:33:10.175218
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:33:11.549609
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:33:12.874860
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:33:14.235839
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:33:15.549353
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:33:16.857394
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:33:18.170906
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:33:19.595606
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:33:21.030840
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:33:22.427637
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:33:45.294681
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:33:47.712164
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:33:50.130922
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:33:52.548979
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:33:54.965257
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:33:57.585460
# Unit test for constructor of class DictToken
def test_DictToken():key_token = ScalarToken("a", 1, 1, '{"a": 1}')

# Generated at 2026-10-24 11:33:58.900589
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:34:00.209649
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:34:01.540322
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:34:02.846388
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:34:04.155989
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:34:05.479723
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:34:06.807176
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:34:08.123724
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:34:51.707263
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:34:54.125045
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:34:56.543279
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:34:58.960402
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:35:01.378825
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:35:03.797367
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:35:06.213727
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:35:08.815264
# Unit test for constructor of class DictToken
def test_DictToken():key_token = ScalarToken("a", 1, 1, '{"a": 1}')

# Generated at 2026-10-24 11:35:10.127329
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:35:11.437746
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:35:12.854775
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:35:14.289546
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:35:15.597934
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:35:16.926360
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:35:18.233483
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"key": "value"}'
    # 0123456789...
    # {"key": "value"}
    key_token = ScalarToken("key", 2, 4, content)      # -> 'key'
    value_token = ScalarToken("value", 8, 14, content)  # -> '"value"'

    token = DictToken({key_token: value_token}, 0, 15, content)

    # value round-trips through the key/value token pairs
    assert token.value == {"key": "value"}
    # string spans the full slice of content
    assert token.string == content
    # child token lookup by key
    assert token._get_child_token("key") == value_token
    assert token._get_key_token("key") == key_token
    # public lookup helpers
    assert token.lookup(["key"]) == value_token
    assert token.lookup_key(["key"]) == key_token

# Generated at 2026-10-24 11:36:43.304357
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:36:45.721936
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:36:48.138669
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:36:50.553580
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:36:52.970488
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:36:55.391365
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:36:57.810665
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:37:00.227927
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:37:02.643339
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:37:05.061337
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:37:07.478299
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:37:09.899054
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:37:12.326270
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:37:14.748022
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:37:17.169311
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:37:19.589991
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:37:22.008573
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:37:24.428757
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:37:26.848432
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:37:29.272933
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:37:31.683464
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:37:34.105940
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:37:36.528495
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:37:38.949769
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:37:41.367204
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:37:43.782611
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:37:46.202196
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:37:48.619829
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:37:51.037337
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 11:37:53.455937
# Unit test for constructor of class DictToken