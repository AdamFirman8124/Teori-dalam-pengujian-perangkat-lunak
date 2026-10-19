

# Generated at 2024-05-31 18:06:13.915192
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:06:21.166727
# Unit test for function parse_kv
def test_parse_kv():    # Test case 1: Basic key-value pairs
    args = "key1=value1 key2=value2"
    expected = {"key1": "value1", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 2: Key-value pairs with spaces
    args = "key1=value1 key2='value with spaces'"
    expected = {"key1": "value1", "key2": "value with spaces"}
    assert parse_kv(args) == expected

    # Test case 3: Key-value pairs with escaped characters
    args = r"key1=value1 key2=value\ with\ spaces"
    expected = {"key1": "value1", "key2": "value with spaces"}
    assert parse_kv(args) == expected

    # Test case 4: Key-value pairs with raw parameters

# Generated at 2024-05-31 18:06:25.321662
# Unit test for function parse_kv
def test_parse_kv():    # Test case 1: Basic key-value pairs
    args = "key1=value1 key2=value2"
    expected = {"key1": "value1", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 2: Key-value pairs with spaces
    args = 'key1="value with spaces" key2=value2'
    expected = {"key1": "value with spaces", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 3: Key-value pairs with escaped characters
    args = r'key1=value\ with\ spaces key2=value2'
    expected = {"key1": "value with spaces", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 4: Key-value pairs with raw parameters

# Generated at 2024-05-31 18:06:28.334939
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:06:32.820799
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:06:36.618023
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:06:40.197818
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:06:44.129412
# Unit test for function parse_kv
def test_parse_kv():    # Test case 1: Basic key-value pairs
    args = "key1=value1 key2=value2"
    expected = {"key1": "value1", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 2: Key-value pairs with spaces
    args = 'key1="value with spaces" key2=value2'
    expected = {"key1": "value with spaces", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 3: Key-value pairs with escaped characters
    args = r'key1=value\ with\ spaces key2=value2'
    expected = {"key1": "value with spaces", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 4: Key-value pairs with raw parameters

# Generated at 2024-05-31 18:06:48.490729
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:06:54.822579
# Unit test for function parse_kv
def test_parse_kv():    # Test case 1: Basic key-value pairs
    args = "key1=value1 key2=value2"
    expected = {"key1": "value1", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 2: Key-value pairs with spaces
    args = "key1='value with spaces' key2=value2"
    expected = {"key1": "value with spaces", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 3: Key-value pairs with escaped characters
    args = "key1=value\\ with\\ spaces key2=value2"
    expected = {"key1": "value with spaces", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 4: Key-value pairs with raw parameters

# Generated at 2024-05-31 18:07:31.088864
# Unit test for function parse_kv
def test_parse_kv():    # Test case 1: Basic key-value pairs
    args = "key1=value1 key2=value2"
    expected = {"key1": "value1", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 2: Key-value pairs with spaces
    args = "key1=value1 key2='value with spaces'"
    expected = {"key1": "value1", "key2": "value with spaces"}
    assert parse_kv(args) == expected

    # Test case 3: Key-value pairs with escaped characters
    args = r"key1=value1 key2=value\ with\ spaces"
    expected = {"key1": "value1", "key2": "value with spaces"}
    assert parse_kv(args) == expected

    # Test case 4: Key-value pairs with raw parameters

# Generated at 2024-05-31 18:07:34.784067
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:07:41.066285
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:07:45.482920
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:07:49.025940
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:07:52.962306
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:07:58.179794
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:08:03.526144
# Unit test for function parse_kv
def test_parse_kv():    # Test case 1: Basic key-value pairs
    args = "key1=value1 key2=value2"
    expected = {"key1": "value1", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 2: Key-value pairs with spaces
    args = 'key1="value with spaces" key2=value2'
    expected = {"key1": "value with spaces", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 3: Key-value pairs with escaped characters
    args = r'key1=value\ with\ spaces key2=value2'
    expected = {"key1": "value with spaces", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 4: Key-value pairs with raw parameters

# Generated at 2024-05-31 18:08:07.810236
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:08:13.646032
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:08:35.757950
# Unit test for function parse_kv
def test_parse_kv():    # Test case 1: Basic key-value pairs
    args = "key1=value1 key2=value2"
    expected = {"key1": "value1", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 2: Key-value pairs with spaces
    args = 'key1="value with spaces" key2=value2'
    expected = {"key1": "value with spaces", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 3: Key-value pairs with escaped characters
    args = r'key1=value\ with\ spaces key2=value2'
    expected = {"key1": "value with spaces", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 4: Key-value pairs with raw parameters

# Generated at 2024-05-31 18:08:39.720861
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:08:43.833651
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:08:49.679454
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:08:53.273870
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:08:56.727982
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:09:01.234154
# Unit test for function parse_kv
def test_parse_kv():    # Test case 1: Basic key-value pairs
    args = "key1=value1 key2=value2"
    expected = {"key1": "value1", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 2: Key-value pairs with spaces
    args = 'key1="value with spaces" key2=value2'
    expected = {"key1": "value with spaces", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 3: Key-value pairs with escaped characters
    args = r'key1=value\ with\ spaces key2=value2'
    expected = {"key1": "value with spaces", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 4: Key-value pairs with raw parameters

# Generated at 2024-05-31 18:09:04.682040
# Unit test for function parse_kv
def test_parse_kv():    # Test case 1: Basic key-value pairs
    args = "key1=value1 key2=value2"
    expected = {"key1": "value1", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 2: Key-value pairs with spaces
    args = 'key1="value with spaces" key2=value2'
    expected = {"key1": "value with spaces", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 3: Key-value pairs with escaped characters
    args = 'key1=value\\ with\\ spaces key2=value2'
    expected = {"key1": "value with spaces", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 4: Key-value pairs with raw parameters

# Generated at 2024-05-31 18:09:08.642442
# Unit test for function parse_kv
def test_parse_kv():    # Test case 1: Basic key-value pairs
    args = "key1=value1 key2=value2"
    expected = {"key1": "value1", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 2: Key-value pairs with spaces
    args = "key1=value1 key2='value with spaces'"
    expected = {"key1": "value1", "key2": "value with spaces"}
    assert parse_kv(args) == expected

    # Test case 3: Key-value pairs with escaped characters
    args = r"key1=value1 key2=value\ with\ spaces"
    expected = {"key1": "value1", "key2": "value with spaces"}
    assert parse_kv(args) == expected

    # Test case 4: Key-value pairs with raw parameters

# Generated at 2024-05-31 18:09:14.085620
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:09:36.372399
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:09:39.913459
# Unit test for function parse_kv
def test_parse_kv():    # Test case 1: Basic key-value pairs
    args = "key1=value1 key2=value2"
    expected = {"key1": "value1", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 2: Key-value pairs with spaces
    args = "key1=value1 key2='value with spaces'"
    expected = {"key1": "value1", "key2": "value with spaces"}
    assert parse_kv(args) == expected

    # Test case 3: Key-value pairs with escaped characters
    args = r"key1=value1 key2=value\=with\=equals"
    expected = {"key1": "value1", "key2": "value=with=equals"}
    assert parse_kv(args) == expected

    # Test case 4: Key-value pairs with raw parameters

# Generated at 2024-05-31 18:09:43.639667
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:09:49.113872
# Unit test for function parse_kv
def test_parse_kv():    # Test case 1: Basic key-value pairs
    args = "key1=value1 key2=value2"
    expected = {"key1": "value1", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 2: Key-value pairs with spaces
    args = "key1=value1 key2='value with spaces'"
    expected = {"key1": "value1", "key2": "value with spaces"}
    assert parse_kv(args) == expected

    # Test case 3: Key-value pairs with escaped characters
    args = r"key1=value1 key2=value\ with\ spaces"
    expected = {"key1": "value1", "key2": "value with spaces"}
    assert parse_kv(args) == expected

    # Test case 4: Key-value pairs with raw parameters

# Generated at 2024-05-31 18:09:53.495480
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:09:56.731993
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:10:00.341844
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:10:06.154466
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:10:11.842634
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:10:16.773866
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:10:30.350093
# Unit test for function parse_kv
def test_parse_kv():    # Test case 1: Basic key-value pairs
    args = "key1=value1 key2=value2"
    expected = {"key1": "value1", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 2: Key-value pairs with spaces
    args = "key1=value1 key2='value with spaces'"
    expected = {"key1": "value1", "key2": "value with spaces"}
    assert parse_kv(args) == expected

    # Test case 3: Key-value pairs with escaped characters
    args = r"key1=value1 key2=value\ with\ spaces"
    expected = {"key1": "value1", "key2": "value with spaces"}
    assert parse_kv(args) == expected

    # Test case 4: Key-value pairs with raw parameters

# Generated at 2024-05-31 18:10:34.512913
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:10:45.230573
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:10:53.479701
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:10:58.005088
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:11:01.649859
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:11:05.427284
# Unit test for function parse_kv
def test_parse_kv():    # Test case 1: Basic key-value pairs
    args = "key1=value1 key2=value2"
    expected = {"key1": "value1", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 2: Key-value pairs with spaces
    args = "key1='value with spaces' key2=value2"
    expected = {"key1": "value with spaces", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 3: Key-value pairs with escaped characters
    args = r"key1=value\ with\ spaces key2=value2"
    expected = {"key1": "value with spaces", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 4: Key-value pairs with raw parameters

# Generated at 2024-05-31 18:11:10.014800
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:11:13.316936
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:11:17.972665
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:11:32.427672
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:11:36.258180
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:11:40.679983
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:11:44.907955
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:11:48.917773
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:11:53.011387
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:11:56.176298
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:11:59.381894
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:12:03.170613
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:12:07.919220
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:12:21.363123
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:12:25.415302
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:12:28.665818
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:12:32.289934
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:12:35.771673
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:12:40.318815
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:12:44.231118
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:12:50.240333
# Unit test for function parse_kv
def test_parse_kv():    # Test case 1: Basic key-value pairs
    args = "key1=value1 key2=value2"
    expected = {"key1": "value1", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 2: Key-value pairs with spaces
    args = 'key1="value with spaces" key2=value2'
    expected = {"key1": "value with spaces", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 3: Key-value pairs with escaped characters
    args = r'key1=value\ with\ spaces key2=value2'
    expected = {"key1": "value with spaces", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 4: Key-value pairs with raw parameters

# Generated at 2024-05-31 18:12:53.636279
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:12:57.274491
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:13:11.816454
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:13:15.317209
# Unit test for function parse_kv
def test_parse_kv():    # Test case 1: Basic key-value pairs
    args = "key1=value1 key2=value2"
    expected = {"key1": "value1", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 2: Key-value pairs with spaces
    args = "key1='value with spaces' key2=value2"
    expected = {"key1": "value with spaces", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 3: Key-value pairs with escaped characters
    args = "key1=value\\ with\\ spaces key2=value2"
    expected = {"key1": "value with spaces", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 4: Key-value pairs with raw parameters

# Generated at 2024-05-31 18:13:18.872855
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:13:22.439874
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:13:25.993436
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:13:29.558023
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:13:33.904454
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:13:37.434310
# Unit test for function parse_kv
def test_parse_kv():    # Test case 1: Basic key-value pairs
    args = "key1=value1 key2=value2"
    expected = {"key1": "value1", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 2: Key-value pairs with spaces
    args = "key1='value with spaces' key2=value2"
    expected = {"key1": "value with spaces", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 3: Key-value pairs with escaped characters
    args = "key1=value\\ with\\ spaces key2=value2"
    expected = {"key1": "value with spaces", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 4: Key-value pairs with raw parameters

# Generated at 2024-05-31 18:13:42.790231
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:13:46.374734
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:14:05.113541
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:14:09.091414
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:14:13.502928
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:14:17.403440
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:14:21.361033
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:14:25.662592
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:14:30.192620
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:14:35.434885
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:14:41.400317
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:14:45.029463
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:15:00.507415
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:15:03.822464
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:15:07.389543
# Unit test for function parse_kv
def test_parse_kv():    # Test case 1: Basic key-value pairs
    args = "key1=value1 key2=value2"
    expected = {"key1": "value1", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 2: Key-value pairs with spaces
    args = "key1=value1 key2='value with spaces'"
    expected = {"key1": "value1", "key2": "value with spaces"}
    assert parse_kv(args) == expected

    # Test case 3: Key-value pairs with escaped characters
    args = r"key1=value1 key2=value\ with\ spaces"
    expected = {"key1": "value1", "key2": "value with spaces"}
    assert parse_kv(args) == expected

    # Test case 4: Key-value pairs with raw parameters

# Generated at 2024-05-31 18:15:10.859325
# Unit test for function parse_kv
def test_parse_kv():    # Test case 1: Basic key-value pairs
    args = "key1=value1 key2=value2"
    expected = {"key1": "value1", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 2: Key-value pairs with spaces
    args = "key1=value1 key2='value with spaces'"
    expected = {"key1": "value1", "key2": "value with spaces"}
    assert parse_kv(args) == expected

    # Test case 3: Key-value pairs with escaped characters
    args = r"key1=value1 key2=value\=with\=equals"
    expected = {"key1": "value1", "key2": "value=with=equals"}
    assert parse_kv(args) == expected

    # Test case 4: Key-value pairs with raw parameters

# Generated at 2024-05-31 18:15:14.802074
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:15:18.212495
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2024-05-31 18:15:21.716835
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:15:26.081592
# Unit test for function split_args
def test_split_args():    assert split_args('a=b c="foo bar"') == ['a=b', 'c="foo bar"']

# Generated at 2024-05-31 18:15:31.847059
# Unit test for function parse_kv
def test_parse_kv():    # Test case 1: Basic key-value pairs
    args = "key1=value1 key2=value2"
    expected = {"key1": "value1", "key2": "value2"}
    assert parse_kv(args) == expected

    # Test case 2: Key-value pairs with spaces and quotes
    args = 'key1="value with spaces" key2=\'another value\''
    expected = {"key1": "value with spaces", "key2": "another value"}
    assert parse_kv(args) == expected

    # Test case 3: Key-value pairs with escaped characters
    args = r'key1=value1 key2=escaped\=value'
    expected = {"key1": "value1", "key2": "escaped=value"}
    assert parse_kv(args) == expected

    # Test case 4: Raw parameters without check_raw

# Generated at 2024-05-31 18:15:34.965756
# Unit test for function parse_kv
def test_parse_kv():    assert parse_kv('key1=value1 key2=value2') == {'key1': 'value1', 'key2': 'value2'}