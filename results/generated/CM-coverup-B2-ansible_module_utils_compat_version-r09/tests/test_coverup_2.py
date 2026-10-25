# file: project/ansible/module_utils/compat/version.py:39-81
# asked: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}
# gained: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}

import pytest

from ansible.module_utils.compat.version import Version


def test_version_init_parses_only_truthy_strings(monkeypatch):
    calls = []

    def parse(instance, vstring):
        calls.append((instance, vstring))
        instance.parsed = vstring

    monkeypatch.setattr(Version, "parse", parse, raising=False)

    no_version = Version()
    empty_version = Version("")
    parsed_version = Version("1.2.3")

    assert calls == [(parsed_version, "1.2.3")]
    assert not hasattr(no_version, "parsed")
    assert not hasattr(empty_version, "parsed")
    assert parsed_version.parsed == "1.2.3"


def test_version_repr_uses_class_name_and_string_value(monkeypatch):
    monkeypatch.setattr(Version, "__str__", lambda self: "1.2.3")

    version = Version()

    assert repr(version) == "Version ('1.2.3')"


@pytest.mark.parametrize(
    ("method_name", "comparison", "expected"),
    [
        ("__eq__", 0, True),
        ("__eq__", 1, False),
        ("__lt__", -1, True),
        ("__lt__", 0, False),
        ("__le__", 0, True),
        ("__le__", 1, False),
        ("__gt__", 1, True),
        ("__gt__", 0, False),
        ("__ge__", 0, True),
        ("__ge__", -1, False),
    ],
)
def test_version_rich_comparisons(monkeypatch, method_name, comparison, expected):
    calls = []

    def cmp(instance, other):
        calls.append((instance, other))
        return comparison

    monkeypatch.setattr(Version, "_cmp", cmp, raising=False)

    version = Version()
    other = object()

    assert getattr(version, method_name)(other) is expected
    assert len(calls) == 1
    assert calls[0][0] is version
    assert calls[0][1] is other


@pytest.mark.parametrize(
    "method_name",
    ["__eq__", "__lt__", "__le__", "__gt__", "__ge__"],
)
def test_version_rich_comparisons_propagate_not_implemented(
    monkeypatch, method_name
):
    calls = []

    def cmp(instance, other):
        calls.append((instance, other))
        return NotImplemented

    monkeypatch.setattr(Version, "_cmp", cmp, raising=False)

    version = Version()
    other = object()

    assert getattr(version, method_name)(other) is NotImplemented
    assert len(calls) == 1
    assert calls[0][0] is version
    assert calls[0][1] is other
