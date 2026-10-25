

# Generated at 2026-10-24 20:17:26.532223
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

# Generated at 2026-10-24 20:17:27.918048
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:17:29.237350
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

# Generated at 2026-10-24 20:17:30.685853
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:17:32.020266
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

# Generated at 2026-10-24 20:17:33.449076
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:17:34.772324
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

# Generated at 2026-10-24 20:17:36.222784
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:17:37.551258
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

# Generated at 2026-10-24 20:17:38.976944
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:17:40.299182
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

# Generated at 2026-10-24 20:17:41.744983
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:17:43.179162
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

# Generated at 2026-10-24 20:17:44.610194
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:17:45.930033
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

# Generated at 2026-10-24 20:17:47.288641
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:17:49.013056
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

# Generated at 2026-10-24 20:17:50.446063
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:17:51.781722
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

# Generated at 2026-10-24 20:17:53.210072
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:17:54.560630
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

# Generated at 2026-10-24 20:17:55.974806
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:17:57.295126
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

# Generated at 2026-10-24 20:17:58.740291
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:18:00.095884
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

# Generated at 2026-10-24 20:18:01.482192
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:18:02.831489
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

# Generated at 2026-10-24 20:18:04.269394
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:18:05.674461
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

# Generated at 2026-10-24 20:18:08.215137
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:18:10.632668
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:18:13.051552
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:18:15.620368
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:18:18.142567
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:18:20.559717
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:18:22.975934
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:18:25.416933
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:18:27.970706
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:18:30.389909
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:18:32.810451
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:18:35.225362
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:18:37.642018
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:18:40.057775
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:18:42.475396
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:18:44.890680
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:18:47.307939
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:18:49.725658
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:18:52.141969
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:18:54.558665
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:18:56.975977
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:18:59.390515
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:19:01.806959
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:19:04.225756
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:19:06.646087
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:19:09.063157
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:19:11.482146
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:19:13.900593
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:19:16.319531
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:19:18.740057
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:19:21.157169
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:19:23.573282
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:19:25.987947
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:19:28.403977
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:19:30.819771
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:19:32.312239
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

# Generated at 2026-10-24 20:19:33.689707
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:19:35.076495
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

# Generated at 2026-10-24 20:19:36.440642
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:19:37.847117
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

# Generated at 2026-10-24 20:19:39.298962
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:19:40.654363
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

# Generated at 2026-10-24 20:19:43.076047
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:19:51.688221
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({"a": 1, "b": 2}) is True

# Generated at 2026-10-24 20:19:53.057205
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

# Generated at 2026-10-24 20:19:54.451587
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:19:55.772979
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

# Generated at 2026-10-24 20:19:57.150965
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:19:58.475765
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

# Generated at 2026-10-24 20:19:59.840124
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:20:01.180952
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

# Generated at 2026-10-24 20:20:02.644092
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:20:03.992926
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

# Generated at 2026-10-24 20:20:05.408256
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:20:06.842663
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

# Generated at 2026-10-24 20:20:08.275305
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:20:09.604591
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

# Generated at 2026-10-24 20:20:10.959908
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:20:12.282463
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

# Generated at 2026-10-24 20:20:13.808107
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:20:15.259977
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

# Generated at 2026-10-24 20:20:16.677642
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:20:18.006398
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

# Generated at 2026-10-24 20:20:19.379248
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:20:21.916162
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:20:24.339452
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:20:26.754946
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:20:29.173245
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:20:31.590978
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:20:34.009157
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:20:36.429043
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:20:38.848489
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:20:41.261311
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:20:43.679264
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:20:46.094304
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:20:47.514436
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:20:48.875653
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

# Generated at 2026-10-24 20:20:50.463259
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:20:51.791591
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

# Generated at 2026-10-24 20:20:53.228450
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:20:54.555403
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

# Generated at 2026-10-24 20:20:55.994607
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:20:57.319049
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

# Generated at 2026-10-24 20:20:58.763174
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:21:00.135174
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

# Generated at 2026-10-24 20:21:01.524043
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:21:02.849735
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

# Generated at 2026-10-24 20:21:04.233317
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:21:05.621905
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

# Generated at 2026-10-24 20:21:07.052324
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:21:08.383869
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

# Generated at 2026-10-24 20:21:09.818134
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:21:11.182169
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

# Generated at 2026-10-24 20:21:12.583344
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:21:13.902069
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

# Generated at 2026-10-24 20:21:15.318660
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 20:21:17.742167
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:21:20.157510
# Unit test for function check_dict_case

# Generated at 2026-10-24 20:21:22.574307
# Unit test for function check_dict_case