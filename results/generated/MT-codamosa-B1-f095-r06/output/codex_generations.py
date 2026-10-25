

# Generated at 2026-10-24 19:53:42.138464
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

# Generated at 2026-10-24 19:53:43.463200
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:53:46.013272
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:53:48.546760
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:53:51.063599
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:53:53.481151
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:53:55.897648
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:53:58.457633
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:54:00.876891
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:54:03.291302
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:54:05.709932
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:54:08.126305
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:54:10.543534
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:54:18.650137
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({"A": 1, "B": 2}) is True

# Generated at 2026-10-24 19:54:19.973847
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

# Generated at 2026-10-24 19:54:21.413401
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:54:22.729285
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

# Generated at 2026-10-24 19:54:24.151761
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:54:25.476284
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

# Generated at 2026-10-24 19:54:26.943969
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:54:28.267101
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

# Generated at 2026-10-24 19:54:29.710530
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:54:31.033596
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

# Generated at 2026-10-24 19:54:32.439742
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:54:33.787023
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

# Generated at 2026-10-24 19:54:35.240409
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:54:36.568177
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

# Generated at 2026-10-24 19:54:38.003040
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:54:39.439195
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

# Generated at 2026-10-24 19:54:40.870094
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:54:42.189356
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

# Generated at 2026-10-24 19:54:43.635146
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:54:45.070012
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

# Generated at 2026-10-24 19:54:46.540225
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:54:47.838876
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

# Generated at 2026-10-24 19:54:49.217205
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:54:51.750074
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:54:54.265581
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:54:56.681272
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:54:59.098211
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:55:01.511183
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:55:04.097080
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:55:06.514471
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:55:08.930444
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:55:11.346786
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:55:13.914881
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:55:16.330783
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:55:18.747704
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:55:21.165789
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:55:23.583021
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:55:25.998245
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:55:28.414416
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:55:30.829934
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:55:33.249738
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:55:35.665250
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:55:38.079708
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:55:40.495446
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:55:42.912534
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:55:45.327489
# Unit test for function check_dict_case

# Generated at 2026-10-24 19:55:56.753611
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) is False

# Generated at 2026-10-24 19:55:58.178553
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

# Generated at 2026-10-24 19:55:59.616472
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:56:00.949503
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

# Generated at 2026-10-24 19:56:02.381027
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:56:03.816296
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

# Generated at 2026-10-24 19:56:05.249135
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:56:06.583575
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

# Generated at 2026-10-24 19:56:08.018484
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:56:09.336641
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

# Generated at 2026-10-24 19:56:10.777867
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:56:12.115446
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

# Generated at 2026-10-24 19:56:13.482330
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:56:14.803266
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

# Generated at 2026-10-24 19:56:16.183274
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:56:17.504598
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

# Generated at 2026-10-24 19:56:18.860148
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:56:20.310224
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

# Generated at 2026-10-24 19:56:21.734252
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:56:23.055622
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

# Generated at 2026-10-24 19:56:24.501385
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 19:56:25.826093
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

# Generated at 2026-10-24 19:56:27.265511
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False