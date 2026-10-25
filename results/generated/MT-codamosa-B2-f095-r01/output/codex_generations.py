

# Generated at 2026-10-24 21:23:41.723044
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

# Generated at 2026-10-24 21:23:43.101102
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:23:44.428048
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

# Generated at 2026-10-24 21:23:45.866692
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:23:47.190937
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

# Generated at 2026-10-24 21:23:48.633300
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:23:50.065755
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

# Generated at 2026-10-24 21:23:52.596334
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:23:55.111380
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:23:57.648516
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:24:00.181560
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:24:02.602122
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:24:05.020966
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:24:12.697079
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) is False

# Generated at 2026-10-24 21:24:14.026064
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

# Generated at 2026-10-24 21:24:15.466306
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:24:16.782850
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

# Generated at 2026-10-24 21:24:18.152446
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:24:19.481410
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

# Generated at 2026-10-24 21:24:20.852043
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:24:22.166370
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

# Generated at 2026-10-24 21:24:23.549703
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:24:24.887312
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

# Generated at 2026-10-24 21:24:26.239247
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:24:27.561826
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

# Generated at 2026-10-24 21:24:29.985019
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:24:32.401864
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:24:34.991482
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:24:37.582126
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:24:40.001388
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:24:42.417726
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:24:44.837246
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:24:47.254934
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:24:49.850114
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:24:52.269731
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:24:54.685664
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:24:57.274006
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:24:59.693343
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:25:02.108121
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:25:04.531169
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:25:06.947792
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:25:09.362346
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:25:11.781429
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:25:19.673496
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({"a": 1, "b": 2}) is True

# Generated at 2026-10-24 21:25:21.006691
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

# Generated at 2026-10-24 21:25:22.372869
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:25:23.694105
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

# Generated at 2026-10-24 21:25:25.053301
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:25:26.392503
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

# Generated at 2026-10-24 21:25:27.755530
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:25:29.093692
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

# Generated at 2026-10-24 21:25:30.469498
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:25:31.786858
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

# Generated at 2026-10-24 21:25:33.142109
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:25:35.759158
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:25:38.174153
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:25:40.723113
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:25:43.138788
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:25:45.555841
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:25:48.149477
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:25:50.567063
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:25:52.983988
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:25:55.403990
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:25:57.824033
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:26:00.241837
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:26:02.664823
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:26:05.080352
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:26:07.495331
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:26:09.912595
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:26:12.329795
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:26:14.751420
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:26:17.164933
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:26:19.583025
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:26:21.998616
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:26:24.420240
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:26:26.831819
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:26:29.249185
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:26:31.666771
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:26:34.086169
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:26:36.504090
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:26:38.921626
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:26:41.513367
# Unit test for function check_dict_case
def test_check_dict_case():
    assert module_0.check_dict_case({"a": "apple", "b": "banana"}) is True
    assert module_0.check_dict_case({"A": "apple", "B": "banana"}) is True
    assert module_0.check_dict_case({"a": "apple", "B": "banana"}) is False
    assert module_0.check_dict_case({"a": "apple", 8: "banana"}) is False
    assert module_0.check_dict_case({"Name": "John", "Age": 30, "City": "New York"}) is False
    assert module_0.check_dict_case({"STATE": "NC", "ZIP": "12345"}) is True
    assert module_0.check_dict_case({}) is False
    assert module_0.check_dict_case({"a": 1}) is True
    assert module_0.check_dict_case({"A": 1}) is True
    assert module_0.check_dict_case({"aB": 1}) is False
    assert module_0.check_dict_case({"123": 1}) is False
    assert module_0.check_dict_case({1: "a", 2: "b"}) is False
    print("All tests passed")


if __name__ == "__main__":
    test_check_dict_case()

# Generated at 2026-10-24 21:26:42.835199
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

# Generated at 2026-10-24 21:26:44.202786
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:26:45.521149
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

# Generated at 2026-10-24 21:26:46.916230
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False