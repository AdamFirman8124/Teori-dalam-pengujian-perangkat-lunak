

# Generated at 2026-10-24 19:24:16.082378
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:24:18.596634
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:24:21.014120
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:24:23.436113
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:24:25.850498
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:24:28.267161
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:24:30.850366
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:24:33.269059
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:24:35.696466
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:24:38.268649
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:24:40.685246
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:24:43.102752
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:24:45.518212
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:24:47.933437
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:24:50.350428
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:24:52.768827
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:24:55.184364
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:24:57.603789
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:25:00.031030
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:25:02.446264
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:25:04.864685
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:25:07.289767
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:25:09.706145
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:25:12.123574
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:25:14.541251
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:25:16.955882
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:25:19.372493
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:25:21.794271
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:25:24.211147
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:25:26.627925
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:25:29.045814
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:25:31.461098
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:25:33.879826
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:25:36.296611
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:25:38.715435
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:25:41.133863
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:25:42.604308
# Unit test for function check_dict_case
def test_check_dict_case():import pytest

@pytest.mark.parametrize("d,expected", [
    # empty
    ({}, False),
    # all lower / all upper
    ({"a": 1, "b": 2}, True),
    ({"A": 1, "B": 2}, True),
    ({"a": 1}, True),
    ({"A": 1}, True),
    # mixed case
    ({"a": 1, "B": 2}, False),
    ({"A": 1, "b": 2}, False),
    ({"a": 1, "b": 2, "C": 3}, False),
    # non-string keys
    ({"a": 1, 2: 2}, False),
    ({1: "a", 2: "b"}, False),
    ({"A": 1, "B": 2, 3: 3}, False),
    ({"A": 1, None: 2}, False),
    # string keys that are neither upper nor lower
    ({"1": 1}, False),
    ({"a": 1, "1": 2}, False),
    ({"A": 1, "a b": 2}, False),   # space breaks isupper/islower
    # digits are ignored by isupper()/islower()
    ({"AB1": 1, "CD2": 2}, True),
])
def test_check_dict_case(d, expected):
    assert module_0.check_dict_case(d) == expected

# Generated at 2026-10-24 19:25:44.057769
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:25:45.429560
# Unit test for function check_dict_case
def test_check_dict_case():import pytest

@pytest.mark.parametrize("d,expected", [
    # empty
    ({}, False),
    # all lower / all upper
    ({"a": 1, "b": 2}, True),
    ({"A": 1, "B": 2}, True),
    ({"a": 1}, True),
    ({"A": 1}, True),
    # mixed case
    ({"a": 1, "B": 2}, False),
    ({"A": 1, "b": 2}, False),
    ({"a": 1, "b": 2, "C": 3}, False),
    # non-string keys
    ({"a": 1, 2: 2}, False),
    ({1: "a", 2: "b"}, False),
    ({"A": 1, "B": 2, 3: 3}, False),
    ({"A": 1, None: 2}, False),
    # string keys that are neither upper nor lower
    ({"1": 1}, False),
    ({"a": 1, "1": 2}, False),
    ({"A": 1, "a b": 2}, False),   # space breaks isupper/islower
    # digits are ignored by isupper()/islower()
    ({"AB1": 1, "CD2": 2}, True),
])
def test_check_dict_case(d, expected):
    assert module_0.check_dict_case(d) == expected

# Generated at 2026-10-24 19:25:46.822494
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:25:48.146627
# Unit test for function check_dict_case
def test_check_dict_case():import pytest

@pytest.mark.parametrize("d,expected", [
    # empty
    ({}, False),
    # all lower / all upper
    ({"a": 1, "b": 2}, True),
    ({"A": 1, "B": 2}, True),
    ({"a": 1}, True),
    ({"A": 1}, True),
    # mixed case
    ({"a": 1, "B": 2}, False),
    ({"A": 1, "b": 2}, False),
    ({"a": 1, "b": 2, "C": 3}, False),
    # non-string keys
    ({"a": 1, 2: 2}, False),
    ({1: "a", 2: "b"}, False),
    ({"A": 1, "B": 2, 3: 3}, False),
    ({"A": 1, None: 2}, False),
    # string keys that are neither upper nor lower
    ({"1": 1}, False),
    ({"a": 1, "1": 2}, False),
    ({"A": 1, "a b": 2}, False),   # space breaks isupper/islower
    # digits are ignored by isupper()/islower()
    ({"AB1": 1, "CD2": 2}, True),
])
def test_check_dict_case(d, expected):
    assert module_0.check_dict_case(d) == expected

# Generated at 2026-10-24 19:25:49.503442
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:25:50.874638
# Unit test for function check_dict_case
def test_check_dict_case():import pytest

@pytest.mark.parametrize("d,expected", [
    # empty
    ({}, False),
    # all lower / all upper
    ({"a": 1, "b": 2}, True),
    ({"A": 1, "B": 2}, True),
    ({"a": 1}, True),
    ({"A": 1}, True),
    # mixed case
    ({"a": 1, "B": 2}, False),
    ({"A": 1, "b": 2}, False),
    ({"a": 1, "b": 2, "C": 3}, False),
    # non-string keys
    ({"a": 1, 2: 2}, False),
    ({1: "a", 2: "b"}, False),
    ({"A": 1, "B": 2, 3: 3}, False),
    ({"A": 1, None: 2}, False),
    # string keys that are neither upper nor lower
    ({"1": 1}, False),
    ({"a": 1, "1": 2}, False),
    ({"A": 1, "a b": 2}, False),   # space breaks isupper/islower
    # digits are ignored by isupper()/islower()
    ({"AB1": 1, "CD2": 2}, True),
])
def test_check_dict_case(d, expected):
    assert module_0.check_dict_case(d) == expected

# Generated at 2026-10-24 19:25:52.353510
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:25:53.662465
# Unit test for function check_dict_case
def test_check_dict_case():import pytest

@pytest.mark.parametrize("d,expected", [
    # empty
    ({}, False),
    # all lower / all upper
    ({"a": 1, "b": 2}, True),
    ({"A": 1, "B": 2}, True),
    ({"a": 1}, True),
    ({"A": 1}, True),
    # mixed case
    ({"a": 1, "B": 2}, False),
    ({"A": 1, "b": 2}, False),
    ({"a": 1, "b": 2, "C": 3}, False),
    # non-string keys
    ({"a": 1, 2: 2}, False),
    ({1: "a", 2: "b"}, False),
    ({"A": 1, "B": 2, 3: 3}, False),
    ({"A": 1, None: 2}, False),
    # string keys that are neither upper nor lower
    ({"1": 1}, False),
    ({"a": 1, "1": 2}, False),
    ({"A": 1, "a b": 2}, False),   # space breaks isupper/islower
    # digits are ignored by isupper()/islower()
    ({"AB1": 1, "CD2": 2}, True),
])
def test_check_dict_case(d, expected):
    assert module_0.check_dict_case(d) == expected

# Generated at 2026-10-24 19:25:55.106720
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:25:56.432450
# Unit test for function check_dict_case
def test_check_dict_case():import pytest

@pytest.mark.parametrize("d,expected", [
    # empty
    ({}, False),
    # all lower / all upper
    ({"a": 1, "b": 2}, True),
    ({"A": 1, "B": 2}, True),
    ({"a": 1}, True),
    ({"A": 1}, True),
    # mixed case
    ({"a": 1, "B": 2}, False),
    ({"A": 1, "b": 2}, False),
    ({"a": 1, "b": 2, "C": 3}, False),
    # non-string keys
    ({"a": 1, 2: 2}, False),
    ({1: "a", 2: "b"}, False),
    ({"A": 1, "B": 2, 3: 3}, False),
    ({"A": 1, None: 2}, False),
    # string keys that are neither upper nor lower
    ({"1": 1}, False),
    ({"a": 1, "1": 2}, False),
    ({"A": 1, "a b": 2}, False),   # space breaks isupper/islower
    # digits are ignored by isupper()/islower()
    ({"AB1": 1, "CD2": 2}, True),
])
def test_check_dict_case(d, expected):
    assert module_0.check_dict_case(d) == expected

# Generated at 2026-10-24 19:25:57.871050
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:25:59.205719
# Unit test for function check_dict_case
def test_check_dict_case():import pytest

@pytest.mark.parametrize("d,expected", [
    # empty
    ({}, False),
    # all lower / all upper
    ({"a": 1, "b": 2}, True),
    ({"A": 1, "B": 2}, True),
    ({"a": 1}, True),
    ({"A": 1}, True),
    # mixed case
    ({"a": 1, "B": 2}, False),
    ({"A": 1, "b": 2}, False),
    ({"a": 1, "b": 2, "C": 3}, False),
    # non-string keys
    ({"a": 1, 2: 2}, False),
    ({1: "a", 2: "b"}, False),
    ({"A": 1, "B": 2, 3: 3}, False),
    ({"A": 1, None: 2}, False),
    # string keys that are neither upper nor lower
    ({"1": 1}, False),
    ({"a": 1, "1": 2}, False),
    ({"A": 1, "a b": 2}, False),   # space breaks isupper/islower
    # digits are ignored by isupper()/islower()
    ({"AB1": 1, "CD2": 2}, True),
])
def test_check_dict_case(d, expected):
    assert module_0.check_dict_case(d) == expected

# Generated at 2026-10-24 19:26:00.635460
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:26:02.071474
# Unit test for function check_dict_case
def test_check_dict_case():import pytest

@pytest.mark.parametrize("d,expected", [
    # empty
    ({}, False),
    # all lower / all upper
    ({"a": 1, "b": 2}, True),
    ({"A": 1, "B": 2}, True),
    ({"a": 1}, True),
    ({"A": 1}, True),
    # mixed case
    ({"a": 1, "B": 2}, False),
    ({"A": 1, "b": 2}, False),
    ({"a": 1, "b": 2, "C": 3}, False),
    # non-string keys
    ({"a": 1, 2: 2}, False),
    ({1: "a", 2: "b"}, False),
    ({"A": 1, "B": 2, 3: 3}, False),
    ({"A": 1, None: 2}, False),
    # string keys that are neither upper nor lower
    ({"1": 1}, False),
    ({"a": 1, "1": 2}, False),
    ({"A": 1, "a b": 2}, False),   # space breaks isupper/islower
    # digits are ignored by isupper()/islower()
    ({"AB1": 1, "CD2": 2}, True),
])
def test_check_dict_case(d, expected):
    assert module_0.check_dict_case(d) == expected

# Generated at 2026-10-24 19:26:03.434304
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:26:06.046229
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:26:08.692570
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:26:11.109825
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:26:13.558792
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:26:16.044042
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:26:18.461843
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:26:20.879497
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:26:23.305309
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:26:25.722453
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:26:28.139712
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:26:30.559866
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:26:32.973052
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:26:35.391297
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:26:37.808387
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:26:40.224965
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:26:42.642941
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:26:45.062326
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:26:47.479149
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:26:49.896573
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:26:52.313367
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:26:54.729630
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:26:57.150344
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:26:59.568172
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:27:01.985294
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:27:04.404066
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:27:06.822620
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:27:09.235633
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:27:11.652343
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:27:13.200869
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:27:14.683557
# Unit test for function check_dict_case
def test_check_dict_case():import pytest

@pytest.mark.parametrize("d,expected", [
    # empty
    ({}, False),
    # all lower / all upper
    ({"a": 1, "b": 2}, True),
    ({"A": 1, "B": 2}, True),
    ({"a": 1}, True),
    ({"A": 1}, True),
    # mixed case
    ({"a": 1, "B": 2}, False),
    ({"A": 1, "b": 2}, False),
    ({"a": 1, "b": 2, "C": 3}, False),
    # non-string keys
    ({"a": 1, 2: 2}, False),
    ({1: "a", 2: "b"}, False),
    ({"A": 1, "B": 2, 3: 3}, False),
    ({"A": 1, None: 2}, False),
    # string keys that are neither upper nor lower
    ({"1": 1}, False),
    ({"a": 1, "1": 2}, False),
    ({"A": 1, "a b": 2}, False),   # space breaks isupper/islower
    # digits are ignored by isupper()/islower()
    ({"AB1": 1, "CD2": 2}, True),
])
def test_check_dict_case(d, expected):
    assert module_0.check_dict_case(d) == expected

# Generated at 2026-10-24 19:27:16.039218
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:27:17.361663
# Unit test for function check_dict_case
def test_check_dict_case():import pytest

@pytest.mark.parametrize("d,expected", [
    # empty
    ({}, False),
    # all lower / all upper
    ({"a": 1, "b": 2}, True),
    ({"A": 1, "B": 2}, True),
    ({"a": 1}, True),
    ({"A": 1}, True),
    # mixed case
    ({"a": 1, "B": 2}, False),
    ({"A": 1, "b": 2}, False),
    ({"a": 1, "b": 2, "C": 3}, False),
    # non-string keys
    ({"a": 1, 2: 2}, False),
    ({1: "a", 2: "b"}, False),
    ({"A": 1, "B": 2, 3: 3}, False),
    ({"A": 1, None: 2}, False),
    # string keys that are neither upper nor lower
    ({"1": 1}, False),
    ({"a": 1, "1": 2}, False),
    ({"A": 1, "a b": 2}, False),   # space breaks isupper/islower
    # digits are ignored by isupper()/islower()
    ({"AB1": 1, "CD2": 2}, True),
])
def test_check_dict_case(d, expected):
    assert module_0.check_dict_case(d) == expected

# Generated at 2026-10-24 19:27:18.756191
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:27:20.109591
# Unit test for function check_dict_case
def test_check_dict_case():import pytest

@pytest.mark.parametrize("d,expected", [
    # empty
    ({}, False),
    # all lower / all upper
    ({"a": 1, "b": 2}, True),
    ({"A": 1, "B": 2}, True),
    ({"a": 1}, True),
    ({"A": 1}, True),
    # mixed case
    ({"a": 1, "B": 2}, False),
    ({"A": 1, "b": 2}, False),
    ({"a": 1, "b": 2, "C": 3}, False),
    # non-string keys
    ({"a": 1, 2: 2}, False),
    ({1: "a", 2: "b"}, False),
    ({"A": 1, "B": 2, 3: 3}, False),
    ({"A": 1, None: 2}, False),
    # string keys that are neither upper nor lower
    ({"1": 1}, False),
    ({"a": 1, "1": 2}, False),
    ({"A": 1, "a b": 2}, False),   # space breaks isupper/islower
    # digits are ignored by isupper()/islower()
    ({"AB1": 1, "CD2": 2}, True),
])
def test_check_dict_case(d, expected):
    assert module_0.check_dict_case(d) == expected

# Generated at 2026-10-24 19:27:21.473356
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:27:22.806106
# Unit test for function check_dict_case
def test_check_dict_case():import pytest

@pytest.mark.parametrize("d,expected", [
    # empty
    ({}, False),
    # all lower / all upper
    ({"a": 1, "b": 2}, True),
    ({"A": 1, "B": 2}, True),
    ({"a": 1}, True),
    ({"A": 1}, True),
    # mixed case
    ({"a": 1, "B": 2}, False),
    ({"A": 1, "b": 2}, False),
    ({"a": 1, "b": 2, "C": 3}, False),
    # non-string keys
    ({"a": 1, 2: 2}, False),
    ({1: "a", 2: "b"}, False),
    ({"A": 1, "B": 2, 3: 3}, False),
    ({"A": 1, None: 2}, False),
    # string keys that are neither upper nor lower
    ({"1": 1}, False),
    ({"a": 1, "1": 2}, False),
    ({"A": 1, "a b": 2}, False),   # space breaks isupper/islower
    # digits are ignored by isupper()/islower()
    ({"AB1": 1, "CD2": 2}, True),
])
def test_check_dict_case(d, expected):
    assert module_0.check_dict_case(d) == expected

# Generated at 2026-10-24 19:27:24.404396
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:27:25.724082
# Unit test for function check_dict_case
def test_check_dict_case():import pytest

@pytest.mark.parametrize("d,expected", [
    # empty
    ({}, False),
    # all lower / all upper
    ({"a": 1, "b": 2}, True),
    ({"A": 1, "B": 2}, True),
    ({"a": 1}, True),
    ({"A": 1}, True),
    # mixed case
    ({"a": 1, "B": 2}, False),
    ({"A": 1, "b": 2}, False),
    ({"a": 1, "b": 2, "C": 3}, False),
    # non-string keys
    ({"a": 1, 2: 2}, False),
    ({1: "a", 2: "b"}, False),
    ({"A": 1, "B": 2, 3: 3}, False),
    ({"A": 1, None: 2}, False),
    # string keys that are neither upper nor lower
    ({"1": 1}, False),
    ({"a": 1, "1": 2}, False),
    ({"A": 1, "a b": 2}, False),   # space breaks isupper/islower
    # digits are ignored by isupper()/islower()
    ({"AB1": 1, "CD2": 2}, True),
])
def test_check_dict_case(d, expected):
    assert module_0.check_dict_case(d) == expected

# Generated at 2026-10-24 19:27:27.079720
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:27:28.402700
# Unit test for function check_dict_case
def test_check_dict_case():import pytest

@pytest.mark.parametrize("d,expected", [
    # empty
    ({}, False),
    # all lower / all upper
    ({"a": 1, "b": 2}, True),
    ({"A": 1, "B": 2}, True),
    ({"a": 1}, True),
    ({"A": 1}, True),
    # mixed case
    ({"a": 1, "B": 2}, False),
    ({"A": 1, "b": 2}, False),
    ({"a": 1, "b": 2, "C": 3}, False),
    # non-string keys
    ({"a": 1, 2: 2}, False),
    ({1: "a", 2: "b"}, False),
    ({"A": 1, "B": 2, 3: 3}, False),
    ({"A": 1, None: 2}, False),
    # string keys that are neither upper nor lower
    ({"1": 1}, False),
    ({"a": 1, "1": 2}, False),
    ({"A": 1, "a b": 2}, False),   # space breaks isupper/islower
    # digits are ignored by isupper()/islower()
    ({"AB1": 1, "CD2": 2}, True),
])
def test_check_dict_case(d, expected):
    assert module_0.check_dict_case(d) == expected

# Generated at 2026-10-24 19:27:29.756258
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:27:31.112510
# Unit test for function check_dict_case
def test_check_dict_case():import pytest

@pytest.mark.parametrize("d,expected", [
    # empty
    ({}, False),
    # all lower / all upper
    ({"a": 1, "b": 2}, True),
    ({"A": 1, "B": 2}, True),
    ({"a": 1}, True),
    ({"A": 1}, True),
    # mixed case
    ({"a": 1, "B": 2}, False),
    ({"A": 1, "b": 2}, False),
    ({"a": 1, "b": 2, "C": 3}, False),
    # non-string keys
    ({"a": 1, 2: 2}, False),
    ({1: "a", 2: "b"}, False),
    ({"A": 1, "B": 2, 3: 3}, False),
    ({"A": 1, None: 2}, False),
    # string keys that are neither upper nor lower
    ({"1": 1}, False),
    ({"a": 1, "1": 2}, False),
    ({"A": 1, "a b": 2}, False),   # space breaks isupper/islower
    # digits are ignored by isupper()/islower()
    ({"AB1": 1, "CD2": 2}, True),
])
def test_check_dict_case(d, expected):
    assert module_0.check_dict_case(d) == expected

# Generated at 2026-10-24 19:27:32.464048
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:27:33.789972
# Unit test for function check_dict_case
def test_check_dict_case():import pytest

@pytest.mark.parametrize("d,expected", [
    # empty
    ({}, False),
    # all lower / all upper
    ({"a": 1, "b": 2}, True),
    ({"A": 1, "B": 2}, True),
    ({"a": 1}, True),
    ({"A": 1}, True),
    # mixed case
    ({"a": 1, "B": 2}, False),
    ({"A": 1, "b": 2}, False),
    ({"a": 1, "b": 2, "C": 3}, False),
    # non-string keys
    ({"a": 1, 2: 2}, False),
    ({1: "a", 2: "b"}, False),
    ({"A": 1, "B": 2, 3: 3}, False),
    ({"A": 1, None: 2}, False),
    # string keys that are neither upper nor lower
    ({"1": 1}, False),
    ({"a": 1, "1": 2}, False),
    ({"A": 1, "a b": 2}, False),   # space breaks isupper/islower
    # digits are ignored by isupper()/islower()
    ({"AB1": 1, "CD2": 2}, True),
])
def test_check_dict_case(d, expected):
    assert module_0.check_dict_case(d) == expected

# Generated at 2026-10-24 19:27:35.165956
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:27:37.684293
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:27:40.199970
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:27:42.616187
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:27:45.031119
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:27:47.446648
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:27:49.862724
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:27:52.281738
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:27:53.669347
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:27:55.044159
# Unit test for function check_dict_case
def test_check_dict_case():import pytest

@pytest.mark.parametrize("d,expected", [
    # empty
    ({}, False),
    # all lower / all upper
    ({"a": 1, "b": 2}, True),
    ({"A": 1, "B": 2}, True),
    ({"a": 1}, True),
    ({"A": 1}, True),
    # mixed case
    ({"a": 1, "B": 2}, False),
    ({"A": 1, "b": 2}, False),
    ({"a": 1, "b": 2, "C": 3}, False),
    # non-string keys
    ({"a": 1, 2: 2}, False),
    ({1: "a", 2: "b"}, False),
    ({"A": 1, "B": 2, 3: 3}, False),
    ({"A": 1, None: 2}, False),
    # string keys that are neither upper nor lower
    ({"1": 1}, False),
    ({"a": 1, "1": 2}, False),
    ({"A": 1, "a b": 2}, False),   # space breaks isupper/islower
    # digits are ignored by isupper()/islower()
    ({"AB1": 1, "CD2": 2}, True),
])
def test_check_dict_case(d, expected):
    assert module_0.check_dict_case(d) == expected

# Generated at 2026-10-24 19:27:56.421458
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:27:57.792009
# Unit test for function check_dict_case
def test_check_dict_case():import pytest

@pytest.mark.parametrize("d,expected", [
    # empty
    ({}, False),
    # all lower / all upper
    ({"a": 1, "b": 2}, True),
    ({"A": 1, "B": 2}, True),
    ({"a": 1}, True),
    ({"A": 1}, True),
    # mixed case
    ({"a": 1, "B": 2}, False),
    ({"A": 1, "b": 2}, False),
    ({"a": 1, "b": 2, "C": 3}, False),
    # non-string keys
    ({"a": 1, 2: 2}, False),
    ({1: "a", 2: "b"}, False),
    ({"A": 1, "B": 2, 3: 3}, False),
    ({"A": 1, None: 2}, False),
    # string keys that are neither upper nor lower
    ({"1": 1}, False),
    ({"a": 1, "1": 2}, False),
    ({"A": 1, "a b": 2}, False),   # space breaks isupper/islower
    # digits are ignored by isupper()/islower()
    ({"AB1": 1, "CD2": 2}, True),
])
def test_check_dict_case(d, expected):
    assert module_0.check_dict_case(d) == expected

# Generated at 2026-10-24 19:27:59.231608
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:28:00.556563
# Unit test for function check_dict_case
def test_check_dict_case():import pytest

@pytest.mark.parametrize("d,expected", [
    # empty
    ({}, False),
    # all lower / all upper
    ({"a": 1, "b": 2}, True),
    ({"A": 1, "B": 2}, True),
    ({"a": 1}, True),
    ({"A": 1}, True),
    # mixed case
    ({"a": 1, "B": 2}, False),
    ({"A": 1, "b": 2}, False),
    ({"a": 1, "b": 2, "C": 3}, False),
    # non-string keys
    ({"a": 1, 2: 2}, False),
    ({1: "a", 2: "b"}, False),
    ({"A": 1, "B": 2, 3: 3}, False),
    ({"A": 1, None: 2}, False),
    # string keys that are neither upper nor lower
    ({"1": 1}, False),
    ({"a": 1, "1": 2}, False),
    ({"A": 1, "a b": 2}, False),   # space breaks isupper/islower
    # digits are ignored by isupper()/islower()
    ({"AB1": 1, "CD2": 2}, True),
])
def test_check_dict_case(d, expected):
    assert module_0.check_dict_case(d) == expected

# Generated at 2026-10-24 19:28:01.992917
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:28:03.322560
# Unit test for function check_dict_case
def test_check_dict_case():import pytest

@pytest.mark.parametrize("d,expected", [
    # empty
    ({}, False),
    # all lower / all upper
    ({"a": 1, "b": 2}, True),
    ({"A": 1, "B": 2}, True),
    ({"a": 1}, True),
    ({"A": 1}, True),
    # mixed case
    ({"a": 1, "B": 2}, False),
    ({"A": 1, "b": 2}, False),
    ({"a": 1, "b": 2, "C": 3}, False),
    # non-string keys
    ({"a": 1, 2: 2}, False),
    ({1: "a", 2: "b"}, False),
    ({"A": 1, "B": 2, 3: 3}, False),
    ({"A": 1, None: 2}, False),
    # string keys that are neither upper nor lower
    ({"1": 1}, False),
    ({"a": 1, "1": 2}, False),
    ({"A": 1, "a b": 2}, False),   # space breaks isupper/islower
    # digits are ignored by isupper()/islower()
    ({"AB1": 1, "CD2": 2}, True),
])
def test_check_dict_case(d, expected):
    assert module_0.check_dict_case(d) == expected

# Generated at 2026-10-24 19:28:06.093020
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:28:07.527653
# Unit test for function check_dict_case
def test_check_dict_case():import pytest

@pytest.mark.parametrize("d,expected", [
    # empty
    ({}, False),
    # all lower / all upper
    ({"a": 1, "b": 2}, True),
    ({"A": 1, "B": 2}, True),
    ({"a": 1}, True),
    ({"A": 1}, True),
    # mixed case
    ({"a": 1, "B": 2}, False),
    ({"A": 1, "b": 2}, False),
    ({"a": 1, "b": 2, "C": 3}, False),
    # non-string keys
    ({"a": 1, 2: 2}, False),
    ({1: "a", 2: "b"}, False),
    ({"A": 1, "B": 2, 3: 3}, False),
    ({"A": 1, None: 2}, False),
    # string keys that are neither upper nor lower
    ({"1": 1}, False),
    ({"a": 1, "1": 2}, False),
    ({"A": 1, "a b": 2}, False),   # space breaks isupper/islower
    # digits are ignored by isupper()/islower()
    ({"AB1": 1, "CD2": 2}, True),
])
def test_check_dict_case(d, expected):
    assert module_0.check_dict_case(d) == expected

# Generated at 2026-10-24 19:28:08.880945
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:28:10.215881
# Unit test for function check_dict_case
def test_check_dict_case():import pytest

@pytest.mark.parametrize("d,expected", [
    # empty
    ({}, False),
    # all lower / all upper
    ({"a": 1, "b": 2}, True),
    ({"A": 1, "B": 2}, True),
    ({"a": 1}, True),
    ({"A": 1}, True),
    # mixed case
    ({"a": 1, "B": 2}, False),
    ({"A": 1, "b": 2}, False),
    ({"a": 1, "b": 2, "C": 3}, False),
    # non-string keys
    ({"a": 1, 2: 2}, False),
    ({1: "a", 2: "b"}, False),
    ({"A": 1, "B": 2, 3: 3}, False),
    ({"A": 1, None: 2}, False),
    # string keys that are neither upper nor lower
    ({"1": 1}, False),
    ({"a": 1, "1": 2}, False),
    ({"A": 1, "a b": 2}, False),   # space breaks isupper/islower
    # digits are ignored by isupper()/islower()
    ({"AB1": 1, "CD2": 2}, True),
])
def test_check_dict_case(d, expected):
    assert module_0.check_dict_case(d) == expected

# Generated at 2026-10-24 19:28:11.587578
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:28:12.907248
# Unit test for function check_dict_case
def test_check_dict_case():import pytest

@pytest.mark.parametrize("d,expected", [
    # empty
    ({}, False),
    # all lower / all upper
    ({"a": 1, "b": 2}, True),
    ({"A": 1, "B": 2}, True),
    ({"a": 1}, True),
    ({"A": 1}, True),
    # mixed case
    ({"a": 1, "B": 2}, False),
    ({"A": 1, "b": 2}, False),
    ({"a": 1, "b": 2, "C": 3}, False),
    # non-string keys
    ({"a": 1, 2: 2}, False),
    ({1: "a", 2: "b"}, False),
    ({"A": 1, "B": 2, 3: 3}, False),
    ({"A": 1, None: 2}, False),
    # string keys that are neither upper nor lower
    ({"1": 1}, False),
    ({"a": 1, "1": 2}, False),
    ({"A": 1, "a b": 2}, False),   # space breaks isupper/islower
    # digits are ignored by isupper()/islower()
    ({"AB1": 1, "CD2": 2}, True),
])
def test_check_dict_case(d, expected):
    assert module_0.check_dict_case(d) == expected

# Generated at 2026-10-24 19:28:15.422221
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:28:17.837835
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:28:20.346293
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:28:22.764114
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:28:25.183357
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:28:27.709281
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:28:30.127204
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:28:32.548425
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:28:34.967117
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:28:37.386804
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:28:39.811201
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:28:42.384504
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:28:44.801426
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:28:47.220980
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:28:49.632480
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:28:52.048550
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:28:54.465418
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:28:56.880720
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:28:59.295043
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:29:01.712928
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:29:04.128824
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:29:06.544258
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:29:08.966567
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:29:12.390590
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:29:14.810244
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:29:17.227142
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:29:19.645822
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:29:22.061256
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:29:24.477686
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:29:26.893238
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:29:29.309102
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:29:31.727135
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:29:34.142676
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:29:36.557474
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:29:38.975091
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:29:41.391437
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:29:43.811048
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:29:46.225860
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:29:48.644575
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:29:51.059018
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:29:53.477567
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:29:55.894710
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:29:58.312170
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:30:00.728615
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:30:03.148009
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:30:05.566345
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:30:07.985011
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:30:10.399885
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:30:12.816577
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:30:15.234019
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:30:17.653516
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:30:20.069686
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:30:22.488137
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:30:27.379434
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:30:29.796471
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:30:32.212400
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:30:34.628755
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:30:37.047910
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:30:39.472207
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:30:41.891711
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:30:44.309341
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:30:46.723844
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:30:49.141936
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:30:51.558302
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:30:53.976089
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:30:56.393785
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:30:58.810310
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:31:01.228321
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:31:03.644876
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:31:06.060527
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:31:08.479024
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:31:10.894990
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:31:13.311072
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:31:15.727985
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:31:18.146039
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:31:20.562571
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:31:22.979941
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:31:25.395453
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:31:27.815275
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:31:30.232084
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:31:32.651200
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:31:35.066996
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:31:37.483094
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:31:46.674519
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:31:49.084654
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:31:51.500540
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:31:53.917577
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:31:56.334586
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:31:58.753796
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:32:01.172279
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:32:03.588083
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:32:06.029502
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:32:08.424565
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:32:10.843247
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:32:13.262040
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:32:15.676314
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:32:18.097650
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:32:20.516822
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:32:22.933116
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:32:25.349459
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:32:27.768680
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:32:30.187521
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:32:32.603208
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:32:35.022552
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:32:37.435589
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:32:39.854098
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:32:42.271348
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:32:44.690212
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:32:47.108559
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:32:49.520688
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:32:51.935451
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:32:54.357498
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:32:56.777539
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:33:16.310294
# Unit test for function check_dict_case
def test_check_dict_case():import pytest

@pytest.mark.parametrize("d,expected", [
    # empty
    ({}, False),
    # all lower / all upper
    ({"a": 1, "b": 2}, True),
    ({"A": 1, "B": 2}, True),
    ({"a": 1}, True),
    ({"A": 1}, True),
    # mixed case
    ({"a": 1, "B": 2}, False),
    ({"A": 1, "b": 2}, False),
    ({"a": 1, "b": 2, "C": 3}, False),
    # non-string keys
    ({"a": 1, 2: 2}, False),
    ({1: "a", 2: "b"}, False),
    ({"A": 1, "B": 2, 3: 3}, False),
    ({"A": 1, None: 2}, False),
    # string keys that are neither upper nor lower
    ({"1": 1}, False),
    ({"a": 1, "1": 2}, False),
    ({"A": 1, "a b": 2}, False),   # space breaks isupper/islower
    # digits are ignored by isupper()/islower()
    ({"AB1": 1, "CD2": 2}, True),
])
def test_check_dict_case(d, expected):
    assert module_0.check_dict_case(d) == expected

# Generated at 2026-10-24 19:33:18.831797
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:33:21.248244
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:33:23.664859
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:33:26.083644
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:33:28.500353
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:33:30.920141
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:33:33.339863
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:33:35.757431
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:33:38.173282
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:33:40.589111
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:33:43.007355
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:33:45.427603
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:33:47.844022
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:33:50.261911
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:33:52.678936
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:33:55.085168
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:33:57.502816
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:33:59.917391
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:34:02.336829
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:34:04.756790
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:34:07.173859
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:34:09.589025
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:34:12.005111
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:34:14.420977
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:34:16.835184
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:34:19.250019
# Unit test for function check_dict_case