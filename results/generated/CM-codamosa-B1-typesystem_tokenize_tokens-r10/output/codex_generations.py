

# Generated at 2026-10-24 05:39:20.183071
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    token = ScalarToken(value="example", start_index=0, end_index=6, content="example")

    assert hash(token) == hash("example")

# Generated at 2026-10-24 05:39:25.611731
# Unit test for method __repr__ of class Token
def test_Token___repr__():
    token = Token(value=None, start_index=1, end_index=3, content="abcde")

    assert repr(token) == "Token('bcd')"

# Generated at 2026-10-24 05:39:28.029381
# Unit test for constructor of class Token

# Generated at 2026-10-24 05:39:30.444760
# Unit test for constructor of class Token

# Generated at 2026-10-24 05:39:32.860058
# Unit test for constructor of class Token

# Generated at 2026-10-24 05:39:35.273448
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:39:37.687429
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:39:40.102868
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:39:42.518680
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:39:44.933167
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:39:51.197491
# Unit test for constructor of class DictToken
def test_DictToken():content = '{"answer": 42}'

# Generated at 2026-10-24 05:40:17.415301
# Unit test for constructor of class DictToken
def test_DictToken():key_one = ScalarToken("name", 1, 6, '{"name": 1}')

# Generated at 2026-10-24 05:40:19.998360
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:40:22.412619
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:40:24.826317
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:40:27.336821
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:40:29.745963
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:40:32.168016
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:40:34.582407
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:40:36.996824
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:40:39.409857
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:40:41.963734
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:40:44.377090
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:40:46.794189
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:40:49.210052
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:40:51.624285
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:40:54.039637
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:40:56.453257
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:41:18.758786
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:41:25.003127
# Unit test for method __eq__ of class Token
def test_Token___eq__():left = ScalarToken("value", 1, 5, " value")

# Generated at 2026-10-24 05:41:35.042406
# Unit test for constructor of class DictToken
def test_DictToken():content = '{"name": "Alice", "age": 30}'

# Generated at 2026-10-24 05:41:37.535835
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:41:40.049966
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:41:42.452676
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:41:44.867881
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:41:47.282135
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:41:49.696596
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:41:52.111848
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:41:54.525119
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:41:56.940060
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:42:06.675739
# Unit test for method __eq__ of class Token
def test_Token___eq__():token = ScalarToken("value", 1, 5, " value")

# Generated at 2026-10-24 05:42:15.380340
# Unit test for constructor of class DictToken
def test_DictToken():content = '{"name": 1}'

# Generated at 2026-10-24 05:42:24.289123
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("foo", 0, 2, "foo")

    assert token == ScalarToken("foo", 0, 2, "foo")
    assert token == ScalarToken("foo", 0, 2, "different content")

    assert token != ScalarToken("bar", 0, 2, "bar")
    assert token != ScalarToken("foo", 1, 2, " foo")
    assert token != ScalarToken("foo", 0, 3, "foo ")
    assert token != "foo"
    assert token != object()

# Generated at 2026-10-24 05:42:35.654536
# Unit test for constructor of class DictToken
def test_DictToken():content = '{"name": "Alice"}'

# Generated at 2026-10-24 05:42:38.181086
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:42:40.599404
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:42:43.010948
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:42:45.428576
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:42:47.988989
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:42:50.402476
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:42:53.250580
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:42:55.663556
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:42:58.077721
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:43:00.495696
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:43:02.910084
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:43:05.328301
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:43:07.738332
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:43:10.156676
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:43:12.570213
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:43:14.986736
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:43:17.403813
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:43:19.819564
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:43:22.235353
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:43:24.653189
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:43:27.068123
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:43:29.483408
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:43:31.894986
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:43:34.314485
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:43:36.734429
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:43:39.152728
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:43:41.578432
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:43:43.990899
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:43:46.408745
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:43:48.826748
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:43:51.247036
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:43:53.659778
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:43:56.075241
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:43:58.490584
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:44:00.905543
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:44:03.320282
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:44:05.735793
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:44:08.148969
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:44:10.563859
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:44:12.978439
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:44:15.393713
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:44:17.809320
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:44:20.222115
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:44:22.649707
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:44:25.064139
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:44:27.477206
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:44:29.894208
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:44:32.309247
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:44:34.724341
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:44:37.136608
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:44:39.550082
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:44:41.963353
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:44:44.380391
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:44:46.794930
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:44:49.206730
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:44:51.620204
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:44:54.036376
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:44:56.451995
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:44:58.865403
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:45:01.281252
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:45:03.692982
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:45:06.106688
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:45:08.520762
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:45:10.934840
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:45:13.349017
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:45:15.763199
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:45:18.177945
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:45:20.592082
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:45:23.007764
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:45:25.421744
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:45:27.834444
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:45:30.253071
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:45:32.664306
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:45:35.076862
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:45:37.492695
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:45:39.904957
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:45:42.319656
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:45:44.732480
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:45:47.147422
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:45:49.559742
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:45:51.975901
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:45:54.389690
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:45:56.804727
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:45:59.225272
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:46:01.636414
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:46:04.048933
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:46:06.463197
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:46:08.875542
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:46:11.291822
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:46:13.704460
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:46:16.121294
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:46:18.531647
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:46:20.943882
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:46:23.356412
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:46:25.771429
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:46:28.186380
# Unit test for method __eq__ of class Token

# Generated at 2026-10-24 05:46:30.603878
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:46:33.015289
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:46:35.429885
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:46:37.842222
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:46:40.256457
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:46:42.673878
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:46:45.085573
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:46:47.497328
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:46:49.913312
# Unit test for constructor of class DictToken

# Generated at 2026-10-24 05:46:59.845135
# Unit test for method __eq__ of class Token
def test_Token___eq__():token = ScalarToken("value", 0, 4, "value")

# Generated at 2026-10-24 05:47:10.090011
# Unit test for constructor of class DictToken
def test_DictToken():content = '{"name":"Alice","age":30}'

# Generated at 2026-10-24 05:47:21.763156
# Unit test for constructor of class DictToken
def test_DictToken():content = '{"name": "Ada", "age": 37}'

# Generated at 2026-10-24 05:47:31.491434
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 1, 3, " value")

    # Tokens are equal when their values and indexes match.
    assert token == ScalarToken("value", 1, 3, "different content")

    # Each compared attribute affects equality.
    assert token != ScalarToken("other", 1, 3, " value")
    assert token != ScalarToken("value", 0, 3, " value")
    assert token != ScalarToken("value", 1, 4, " value")

    # A Token is never equal to an unrelated object.
    assert token.__eq__("value") is False
    assert token.__eq__(None) is False

# Generated at 2026-10-24 05:47:40.706386
# Unit test for constructor of class DictToken
def test_DictToken():content = '{"name": "Alice"}'

# Generated at 2026-10-24 05:47:52.125528
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 1, 5, " value")

    # Tokens are equal when their values and indexes match.
    assert token == ScalarToken("value", 1, 5, " value")

    # Content itself is not part of the equality comparison.
    assert token == ScalarToken("value", 1, 5, " different content")

    # Value and both indexes participate in equality.
    assert token != ScalarToken("different", 1, 5, " value")
    assert token != ScalarToken("value", 0, 5, " value")
    assert token != ScalarToken("value", 1, 6, " value")

    # Objects that are not Token instances are never equal.
    assert token != "value"
    assert token != object()

# Generated at 2026-10-24 05:48:04.366634
# Unit test for constructor of class DictToken
def test_DictToken():content = '{"a": 1, "b": true}'

# Generated at 2026-10-24 05:48:12.879043
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 1, 5, " value")

    assert token == token
    assert token == ScalarToken("value", 1, 5, " value")
    assert token == ScalarToken("value", 1, 5, "different content")

    assert token != ScalarToken("other", 1, 5, " value")
    assert token != ScalarToken("value", 0, 5, " value")
    assert token != ScalarToken("value", 1, 4, " value")
    assert token != "value"
    assert token != None  # noqa: E711

# Generated at 2026-10-24 05:48:22.077573
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken("value", 1, 3, "abcd")

    # Equality depends on value and start/end indexes.
    assert token == ScalarToken("value", 1, 3, "wxyz")

    # Content itself is not considered.
    assert token.string != ScalarToken("value", 1, 3, "wxyz").string

    assert token != ScalarToken("different", 1, 3, "abcd")
    assert token != ScalarToken("value", 0, 3, "abcd")
    assert token != ScalarToken("value", 1, 2, "abcd")

    # Objects that are not Token instances are never equal.
    assert token != "value"
    assert token != object()

# Generated at 2026-10-24 05:48:33.749631
# Unit test for constructor of class DictToken
def test_DictToken():content = '{"name": "Alice", "age": 30}'

# Generated at 2026-10-24 05:48:48.399274
# Unit test for constructor of class DictToken
def test_DictToken():content = '{"name": "Alice"}'

# Generated at 2026-10-24 05:48:57.712018
# Unit test for constructor of class DictToken
def test_DictToken():content = '{"name": "Alice"}'

# Generated at 2026-10-24 05:49:07.864740
# Unit test for constructor of class DictToken
def test_DictToken():content = '{"key":"value"}'

# Generated at 2026-10-24 05:49:22.494154
# Unit test for constructor of class DictToken
def test_DictToken():content = '{"name": 42}'