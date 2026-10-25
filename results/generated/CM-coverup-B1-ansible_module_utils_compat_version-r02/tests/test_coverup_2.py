# file: project/ansible/module_utils/compat/version.py:39-81
# asked: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}
# gained: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}

import pytest

from ansible.module_utils.compat.version import Version


class _Version(Version):
    """Minimal concrete Version subclass used to exercise the base class."""

    def __init__(self, vstring=None, cmp_result=0):
        self.cmp_result = cmp_result
        self.parsed = None
        super().__init__(vstring)

    def parse(self, vstring):
        self.parsed = vstring

    def __str__(self):
        return self.parsed if self.parsed is not None else ''

    def _cmp(self, other):
        return self.cmp_result


def test_init_parses_truthy_vstring():
    v = _Version('1.2.3')
    assert v.parsed == '1.2.3'


def test_init_skips_parse_for_falsy_vstring():
    assert _Version().parsed is None
    assert _Version('').parsed is None


def test_repr_includes_class_name_and_str():
    assert repr(_Version('1.2.3')) == "_Version ('1.2.3')"
    assert repr(_Version()) == "_Version ('')"


@pytest.mark.parametrize(
    'cmp_result, expected',
    [(0, True), (1, False), (-1, False)],
)
def test_eq_returns_comparison_result(cmp_result, expected):
    v = _Version(cmp_result=cmp_result)
    assert Version.__eq__(v, object()) is expected


@pytest.mark.parametrize(
    'cmp_result, expected',
    [(-1, True), (0, False), (1, False)],
)
def test_lt_returns_comparison_result(cmp_result, expected):
    v = _Version(cmp_result=cmp_result)
    assert Version.__lt__(v, object()) is expected


@pytest.mark.parametrize(
    'cmp_result, expected',
    [(-1, True), (0, True), (1, False)],
)
def test_le_returns_comparison_result(cmp_result, expected):
    v = _Version(cmp_result=cmp_result)
    assert Version.__le__(v, object()) is expected


@pytest.mark.parametrize(
    'cmp_result, expected',
    [(1, True), (0, False), (-1, False)],
)
def test_gt_returns_comparison_result(cmp_result, expected):
    v = _Version(cmp_result=cmp_result)
    assert Version.__gt__(v, object()) is expected


@pytest.mark.parametrize(
    'cmp_result, expected',
    [(1, True), (0, True), (-1, False)],
)
def test_ge_returns_comparison_result(cmp_result, expected):
    v = _Version(cmp_result=cmp_result)
    assert Version.__ge__(v, object()) is expected


@pytest.mark.parametrize(
    'method_name',
    ['__eq__', '__lt__', '__le__', '__gt__', '__ge__'],
)
def test_comparisons_return_notimplemented(method_name):
    v = _Version(cmp_result=NotImplemented)
    method = getattr(Version, method_name)
    assert method(v, object()) is NotImplemented


def test_notimplemented_falls_back_to_identity_for_eq():
    v = _Version(cmp_result=NotImplemented)
    assert (v == object()) is False


def test_notimplemented_raises_typeerror_for_ordering():
    v = _Version(cmp_result=NotImplemented)
    with pytest.raises(TypeError):
        v < object()


def test_operators_use_cmp_result():
    assert _Version(cmp_result=0) == _Version()
    assert _Version(cmp_result=-1) < _Version()
    assert _Version(cmp_result=-1) <= _Version()
    assert _Version(cmp_result=1) > _Version()
    assert _Version(cmp_result=1) >= _Version()
