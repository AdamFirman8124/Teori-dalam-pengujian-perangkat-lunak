

# Generated at 2026-10-24 21:45:15.645555
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

# Generated at 2026-10-24 21:45:17.034140
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:45:18.423174
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

# Generated at 2026-10-24 21:45:19.904054
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:45:21.336180
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

# Generated at 2026-10-24 21:45:22.770426
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:45:24.112096
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

# Generated at 2026-10-24 21:45:25.474261
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:45:26.799873
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

# Generated at 2026-10-24 21:45:28.191562
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:45:29.546920
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

# Generated at 2026-10-24 21:45:30.914764
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:45:33.437109
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:45:35.954424
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:45:38.471848
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:45:41.010327
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:45:43.432363
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:45:45.849570
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:45:48.437559
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:45:50.854121
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:45:53.435528
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:45:55.850810
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:45:58.266965
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:46:00.686767
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:46:02.052171
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

# Generated at 2026-10-24 21:46:03.496446
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:46:04.848872
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

# Generated at 2026-10-24 21:46:06.288814
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:46:07.617150
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

# Generated at 2026-10-24 21:46:09.053510
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:46:10.386683
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

# Generated at 2026-10-24 21:46:11.817694
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:46:13.141206
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

# Generated at 2026-10-24 21:46:14.582455
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:46:15.916423
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

# Generated at 2026-10-24 21:46:17.348168
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:46:18.683153
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

# Generated at 2026-10-24 21:46:20.050541
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:46:21.444528
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

# Generated at 2026-10-24 21:46:22.877094
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:46:24.312597
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

# Generated at 2026-10-24 21:46:25.755637
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:46:27.078481
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

# Generated at 2026-10-24 21:46:28.509771
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:46:31.054703
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:46:33.675498
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:46:36.094866
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:46:38.509796
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:46:41.027234
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:46:43.547978
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:46:45.967287
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:46:48.390957
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:46:50.809638
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:46:53.333280
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:46:55.751788
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:46:58.171970
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:47:00.588929
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:47:02.036727
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:47:03.375179
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

# Generated at 2026-10-24 21:47:04.763611
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:47:06.115321
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

# Generated at 2026-10-24 21:47:07.534885
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:47:08.892554
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

# Generated at 2026-10-24 21:47:10.277161
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:47:11.612779
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

# Generated at 2026-10-24 21:47:12.966560
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:47:14.295188
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

# Generated at 2026-10-24 21:47:15.679551
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:47:17.001489
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

# Generated at 2026-10-24 21:47:18.360290
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:47:19.697285
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

# Generated at 2026-10-24 21:47:21.067120
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:47:22.385071
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

# Generated at 2026-10-24 21:47:24.919442
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:47:27.340486
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:47:29.758960
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:47:32.177631
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:47:34.594848
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:47:37.011579
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:47:39.430803
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:47:41.845464
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:47:44.354290
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:47:46.794803
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:47:49.210311
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:47:51.631985
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:47:54.045647
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:47:56.463603
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:47:58.882272
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:48:01.298920
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:48:03.719296
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:48:06.135739
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:48:08.557691
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:48:10.971100
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:48:13.390148
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:48:15.807361
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:48:18.227638
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:48:20.639750
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:48:23.059696
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:48:25.478115
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:48:27.896187
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:48:30.313946
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:48:32.731941
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:48:35.145494
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:48:36.565069
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:48:37.878785
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

# Generated at 2026-10-24 21:48:39.581714
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:48:40.914552
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

# Generated at 2026-10-24 21:48:42.346323
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:48:44.020123
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

# Generated at 2026-10-24 21:48:45.376888
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:48:46.721130
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

# Generated at 2026-10-24 21:48:48.090128
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:48:49.434397
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

# Generated at 2026-10-24 21:48:50.795418
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:48:52.133854
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

# Generated at 2026-10-24 21:48:53.610377
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:48:54.937774
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

# Generated at 2026-10-24 21:48:56.380218
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:48:57.710004
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

# Generated at 2026-10-24 21:48:59.140612
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:49:01.563033
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:49:03.981241
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:49:06.505864
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:49:08.920992
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:49:11.338015
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:49:13.755610
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:49:16.171266
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:49:18.591792
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:49:21.015237
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:49:23.429083
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:49:25.845045
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:49:28.428459
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:49:33.408265
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:49:35.823674
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:49:38.241646
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:49:40.661913
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:49:43.080850
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:49:45.499175
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:49:47.917557
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:49:50.333554
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:49:52.752805
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:49:55.168437
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:49:57.585031
# Unit test for function check_dict_case

# Generated at 2026-10-24 21:50:04.475167
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({"a": 1, "b": 2, "C": 3}) is False

# Generated at 2026-10-24 21:50:05.849703
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

# Generated at 2026-10-24 21:50:07.339036
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:50:08.669543
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

# Generated at 2026-10-24 21:50:10.103817
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:50:11.436256
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

# Generated at 2026-10-24 21:50:12.868385
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:50:14.190697
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

# Generated at 2026-10-24 21:50:15.567012
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:50:16.885680
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

# Generated at 2026-10-24 21:50:18.244615
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False

# Generated at 2026-10-24 21:50:19.630472
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

# Generated at 2026-10-24 21:50:21.005372
# Unit test for function check_dict_case
def test_check_dict_case():assert module_0.check_dict_case({}) == False