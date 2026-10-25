

# Generated at 2026-10-25 01:27:04.251602
# Unit test for constructor of class Version

# Generated at 2026-10-25 01:27:06.667141
# Unit test for constructor of class Version

# Generated at 2026-10-25 01:27:09.082726
# Unit test for constructor of class Version

# Generated at 2026-10-25 01:27:11.499232
# Unit test for constructor of class LooseVersion

# Generated at 2026-10-25 01:27:13.915703
# Unit test for constructor of class LooseVersion

# Generated at 2026-10-25 01:27:24.479773
# Unit test for constructor of class LooseVersion
def test_LooseVersion():v = LooseVersion("1.5.2b2")

# Generated at 2026-10-25 01:27:31.448142
# Unit test for method __repr__ of class Version
def test_Version___repr__():
    class ConcreteVersion(Version):
        def __str__(self):
            return "1.2.3"

    version = ConcreteVersion()
    assert repr(version) == "ConcreteVersion ('1.2.3')"

# Generated at 2026-10-25 01:27:42.168001
# Unit test for method __repr__ of class Version

# Generated at 2026-10-25 01:27:43.498779
# Unit test for method __repr__ of class Version

# Generated at 2026-10-25 01:27:52.004367
# Unit test for constructor of class Version

# Generated at 2026-10-25 01:28:07.255578
# Unit test for constructor of class Version

# Generated at 2026-10-25 01:28:09.679073
# Unit test for constructor of class Version

# Generated at 2026-10-25 01:28:12.203035
# Unit test for constructor of class StrictVersion

# Generated at 2026-10-25 01:28:14.619598
# Unit test for constructor of class StrictVersion

# Generated at 2026-10-25 01:28:17.034599
# Unit test for constructor of class StrictVersion

# Generated at 2026-10-25 01:28:39.396321
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    class TestVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    equal_version = TestVersion(0)
    assert equal_version.__eq__(other) is True
    assert equal_version.compared_with is other

    for result in (-1, 1):
        unequal_version = TestVersion(result)
        assert unequal_version.__eq__(other) is False
        assert unequal_version.compared_with is other

    unsupported_version = TestVersion(NotImplemented)
    assert unsupported_version.__eq__(other) is NotImplemented
    assert unsupported_version.compared_with is other

# Generated at 2026-10-25 01:28:45.861339
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    class DummyVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    for comparison_result, expected in [(-1, True), (0, False), (1, False)]:
        version = DummyVersion(comparison_result)
        assert version.__lt__(other) is expected
        assert version.compared_with is other

    version = DummyVersion(NotImplemented)
    assert version.__lt__(other) is NotImplemented
    assert version.compared_with is other

# Generated at 2026-10-25 01:28:55.270232
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    class StubVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    for comparison_result, expected in [
        (-1, False),
        (0, True),
        (1, True),
        (NotImplemented, NotImplemented),
    ]:
        version = StubVersion(comparison_result)

        assert version.__ge__(other) is expected
        assert version.compared_with is other

# Generated at 2026-10-25 01:29:02.142925
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    class TestVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    for comparison_result, expected in (
        (-1, True),
        (0, False),
        (1, False),
    ):
        version = TestVersion(comparison_result)
        assert version.__lt__(other) is expected
        assert version.compared_with is other

    version = TestVersion(NotImplemented)
    assert version.__lt__(other) is NotImplemented
    assert version.compared_with is other

# Generated at 2026-10-25 01:29:04.560121
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 01:29:06.976252
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 01:29:09.392174
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 01:29:11.913409
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:29:14.329648
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:29:16.746182
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:29:19.161116
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 01:29:21.577038
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 01:29:23.991448
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 01:29:26.410673
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 01:29:28.825738
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 01:29:31.241604
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 01:29:33.657605
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 01:29:36.075142
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 01:29:38.492579
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 01:29:40.909087
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 01:29:43.323595
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 01:29:50.616001
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():v = StrictVersion()

# Generated at 2026-10-25 01:29:59.143072
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    test_cases = [
        ("0.4", "0.4"),
        ("0.4.0", "0.4"),
        ("1.0.4", "1.0.4"),
        ("0.5a1", "0.5a1"),
        ("1.0.4b3", "1.0.4b3"),
        ("01.02.003b04", "1.2.3b4"),
        ("1.2.0a3", "1.2a3"),
    ]

    for vstring, expected in test_cases:
        assert str(StrictVersion(vstring)) == expected

# Generated at 2026-10-25 01:30:06.662875
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    class DummyVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    for comparison_result, expected in (
        (-1, True),
        (0, False),
        (1, False),
    ):
        version = DummyVersion(comparison_result)
        assert version.__lt__(other) is expected
        assert version.compared_with is other

    version = DummyVersion(NotImplemented)
    assert version.__lt__(other) is NotImplemented
    assert version.compared_with is other

# Generated at 2026-10-25 01:30:23.142253
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    class DummyVersion(Version):
        def parse(self, vstring):
            self.vstring = str(vstring)
            self.value = int(self.vstring)

        def __str__(self):
            return self.vstring

        def _cmp(self, other):
            if isinstance(other, str):
                other = DummyVersion(other)
            elif not isinstance(other, DummyVersion):
                return NotImplemented
            return (self.value > other.value) - (self.value < other.value)

    # _cmp() == 0 -> True
    assert DummyVersion("1") == DummyVersion("1")
    assert DummyVersion("1") == "1"
    assert DummyVersion("2") == DummyVersion("2")

    # _cmp() < 0 or > 0 -> False
    assert not (DummyVersion("1") == DummyVersion("2"))
    assert not (DummyVersion("2") == DummyVersion("1"))
    assert not (DummyVersion("1") == "2")
    assert DummyVersion("1") != DummyVersion("2")

    # _cmp() is NotImplemented -> __eq__ returns NotImplemented
    assert DummyVersion("1").__eq__(object()) is NotImplemented
    assert DummyVersion("1").__eq__(1) is NotImplemented
    assert not (DummyVersion("1") == object())

# Generated at 2026-10-25 01:30:25.564629
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 01:30:28.137819
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 01:30:30.551989
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 01:30:32.964853
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:30:35.379740
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:30:37.794375
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:30:40.314480
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 01:30:42.727402
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 01:30:45.143247
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 01:30:47.559026
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 01:30:49.973418
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 01:30:52.387797
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 01:30:54.802828
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 01:30:59.601660
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():assert str(StrictVersion("1.2")) == "1.2"

# Generated at 2026-10-25 01:31:14.826713
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    version_1 = ComparableVersion(1)
    equal_version = ComparableVersion(1)
    different_version = ComparableVersion(2)

    assert version_1 == equal_version
    assert not (version_1 == different_version)

    # __eq__ must propagate NotImplemented for unsupported types.
    assert version_1.__eq__(object()) is NotImplemented

# Generated at 2026-10-25 01:31:21.844558
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    class DummyVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    for result, expected in [
        (-1, False),
        (0, True),
        (1, True),
        (NotImplemented, NotImplemented),
    ]:
        version = DummyVersion(result)
        assert version.__ge__(other) is expected
        assert version.compared_with is other

# Generated at 2026-10-25 01:31:28.473567
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    cases = [
        ("0.4", "0.4"),
        ("0.4.0", "0.4"),
        ("0.4.1", "0.4.1"),
        ("1.0a1", "1.0a1"),
        ("1.0.4b3", "1.0.4b3"),
        ("1.0.0a1", "1.0a1"),
        ("01.02.003b04", "1.2.3b4"),
    ]

    for version_string, expected in cases:
        assert str(StrictVersion(version_string)) == expected

# Generated at 2026-10-25 01:31:29.839832
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    # valid string -> (expected .version, expected .prerelease)
    valid = {
        "0.4":     ((0, 4, 0), None),
        "0.4.0":   ((0, 4, 0), None),  # equivalent to 0.4
        "0.4.1":   ((0, 4, 1), None),
        "0.5a1":   ((0, 5, 0), ("a", 1)),
        "0.5b3":   ((0, 5, 0), ("b", 3)),
        "0.5":     ((0, 5, 0), None),
        "0.9.6":   ((0, 9, 6), None),
        "1.0":     ((1, 0, 0), None),
        "1.0.4a3": ((1, 0, 4), ("a", 3)),
        "1.0.4b1": ((1, 0, 4), ("b", 1)),
        "1.0.4":   ((1, 0, 4), None),
        "1.2.3":   ((1, 2, 3), None),
        "1.0a0":   ((1, 0, 0), ("a", 0)),
        "10.20.30b10": ((10, 20, 30), ("b", 10)),
    }


# Generated at 2026-10-25 01:31:46.291628
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    class DummyVersion(Version):
        def parse(self, vstring):
            self.vstring = str(vstring)
            self.value = int(self.vstring)

        def __str__(self):
            return self.vstring

        def _cmp(self, other):
            if isinstance(other, str):
                other = DummyVersion(other)
            elif not isinstance(other, DummyVersion):
                return NotImplemented
            return (self.value > other.value) - (self.value < other.value)

    # _cmp() == 0 -> True
    assert DummyVersion("1") == DummyVersion("1")
    assert DummyVersion("1") == "1"
    assert DummyVersion("2") == DummyVersion("2")

    # _cmp() < 0 or > 0 -> False
    assert not (DummyVersion("1") == DummyVersion("2"))
    assert not (DummyVersion("2") == DummyVersion("1"))
    assert not (DummyVersion("1") == "2")
    assert DummyVersion("1") != DummyVersion("2")

    # _cmp() is NotImplemented -> __eq__ returns NotImplemented
    assert DummyVersion("1").__eq__(object()) is NotImplemented
    assert DummyVersion("1").__eq__(1) is NotImplemented
    assert not (DummyVersion("1") == object())

# Generated at 2026-10-25 01:31:48.710957
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 01:31:51.125301
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 01:31:53.695638
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 01:31:56.112308
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 01:32:13.427387
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 01:32:19.468579
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 01:32:42.622333
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    class TestVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    version = TestVersion(0)
    assert version.__eq__(other) is True
    assert version.compared_with is other

    version = TestVersion(-1)
    assert version.__eq__(other) is False

    version = TestVersion(1)
    assert version.__eq__(other) is False

    version = TestVersion(NotImplemented)
    assert version.__eq__(other) is NotImplemented

# Generated at 2026-10-25 01:33:06.779369
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    sentinel = object()

    class StubVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result

        def _cmp(self, other):
            assert other is sentinel
            return self.comparison_result

    assert StubVersion(1).__gt__(sentinel) is True
    assert StubVersion(0).__gt__(sentinel) is False
    assert StubVersion(-1).__gt__(sentinel) is False
    assert StubVersion(NotImplemented).__gt__(sentinel) is NotImplemented

# Generated at 2026-10-25 01:33:32.354356
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    class ConcreteVersion(Version):
        """Minimal concrete subclass; Version._cmp is abstract."""
        def __init__(self, value):
            self.value = value
            super(ConcreteVersion, self).__init__()

        def _cmp(self, other):
            if isinstance(other, ConcreteVersion):
                other = other.value
            if not isinstance(other, (int, float)):
                return NotImplemented
            if self.value > other:
                return 1
            elif self.value < other:
                return -1
            return 0

    v = ConcreteVersion(2)

    # Greater-than cases
    assert v > 1
    assert v > ConcreteVersion(1)

    # Not-greater cases
    assert not (v > 2)
    assert not (v > 3)
    assert not (v > ConcreteVersion(3))

    # NotImplemented propagation: comparing against an unsupported
    # type must return NotImplemented, not raise or return False.
    assert v.__gt__("not-a-version") is NotImplemented
    assert v.__gt__(None) is NotImplemented

    # Rich comparison delegates through Version.__gt__, so the bool
    # of the reflected comparison must be handled by the other operand
    # (Python falls back / raises TypeError as appropriate).
    try:
        v > object()
        raised = False
    except TypeError:
        raised = True
    assert raised, "comparison with unsupported type should raise TypeError"

# Generated at 2026-10-25 01:33:56.068149
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    class TestVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    for comparison_result, expected in [
        (-1, False),
        (0, False),
        (1, True),
    ]:
        version = TestVersion(comparison_result)
        assert version.__gt__(other) is expected
        assert version.compared_with is other

    version = TestVersion(NotImplemented)
    assert version.__gt__(other) is NotImplemented
    assert version.compared_with is other

# Generated at 2026-10-25 01:33:58.487067
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 01:34:00.902138
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 01:34:03.318086
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 01:34:05.732897
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:34:08.148188
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:34:10.562984
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:34:12.978219
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 01:34:15.393729
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 01:34:17.807665
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 01:34:20.222309
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:34:22.637316
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:34:25.051103
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:34:27.466890
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:34:29.881473
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:34:32.298238
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:34:39.655749
# Unit test for method __le__ of class Version
def test_Version___le__():
    class StubVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result

        def _cmp(self, other):
            return self.comparison_result

    other = object()

    assert StubVersion(-1).__le__(other) is True
    assert StubVersion(0).__le__(other) is True
    assert StubVersion(1).__le__(other) is False
    assert StubVersion(NotImplemented).__le__(other) is NotImplemented

# Generated at 2026-10-25 01:34:45.551529
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    class StubVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result

        def _cmp(self, other):
            return self.comparison_result

    other = object()

    assert StubVersion(1).__ge__(other) is True
    assert StubVersion(0).__ge__(other) is True
    assert StubVersion(-1).__ge__(other) is False
    assert StubVersion(NotImplemented).__ge__(other) is NotImplemented

# Generated at 2026-10-25 01:34:53.376773
# Unit test for method __le__ of class Version
def test_Version___le__():
    class StubVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    for comparison_result, expected in [(-1, True), (0, True), (1, False)]:
        version = StubVersion(comparison_result)
        assert version.__le__(other) is expected
        assert version.compared_with is other

    version = StubVersion(NotImplemented)
    assert version.__le__(other) is NotImplemented
    assert version.compared_with is other

# Generated at 2026-10-25 01:35:02.086989
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    class StubVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    for comparison_result, expected in [
        (-1, False),
        (0, True),
        (1, True),
        (NotImplemented, NotImplemented),
    ]:
        version = StubVersion(comparison_result)
        assert version.__ge__(other) is expected
        assert version.compared_with is other

# Generated at 2026-10-25 01:35:20.064372
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:35:22.478886
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:35:24.893417
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:35:27.308021
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 01:35:29.722653
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 01:35:32.302715
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 01:35:34.716869
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:35:37.131229
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:35:39.545601
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:35:56.046326
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    class ConcreteVersion(Version):
        """Minimal concrete subclass; Version._cmp is abstract."""
        def __init__(self, value):
            self.value = value
            super(ConcreteVersion, self).__init__()

        def _cmp(self, other):
            if isinstance(other, ConcreteVersion):
                other = other.value
            if not isinstance(other, (int, float)):
                return NotImplemented
            if self.value > other:
                return 1
            elif self.value < other:
                return -1
            return 0

    v = ConcreteVersion(2)

    # Greater-than cases
    assert v > 1
    assert v > ConcreteVersion(1)

    # Not-greater cases
    assert not (v > 2)
    assert not (v > 3)
    assert not (v > ConcreteVersion(3))

    # NotImplemented propagation: comparing against an unsupported
    # type must return NotImplemented, not raise or return False.
    assert v.__gt__("not-a-version") is NotImplemented
    assert v.__gt__(None) is NotImplemented

    # Rich comparison delegates through Version.__gt__, so the bool
    # of the reflected comparison must be handled by the other operand
    # (Python falls back / raises TypeError as appropriate).
    try:
        v > object()
        raised = False
    except TypeError:
        raised = True
    assert raised, "comparison with unsupported type should raise TypeError"

# Generated at 2026-10-25 01:36:04.575148
# Unit test for method __le__ of class Version
def test_Version___le__():
    class StubVersion(Version):
        def __init__(self, cmp_result):
            self.cmp_result = cmp_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.cmp_result

    other = object()

    for cmp_result, expected in (
        (-1, True),
        (0, True),
        (1, False),
        (NotImplemented, NotImplemented),
    ):
        version = StubVersion(cmp_result)
        assert version.__le__(other) is expected
        assert version.compared_with is other

# Generated at 2026-10-25 01:36:11.103959
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    class TestVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    version = TestVersion(-1)
    assert version.__lt__(other) is True
    assert version.compared_with is other

    version = TestVersion(0)
    assert version.__lt__(other) is False
    assert version.compared_with is other

    version = TestVersion(1)
    assert version.__lt__(other) is False
    assert version.compared_with is other

    version = TestVersion(NotImplemented)
    assert version.__lt__(other) is NotImplemented
    assert version.compared_with is other

# Generated at 2026-10-25 01:36:12.532746
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    # valid string -> (expected .version, expected .prerelease)
    valid = {
        "0.4":     ((0, 4, 0), None),
        "0.4.0":   ((0, 4, 0), None),  # equivalent to 0.4
        "0.4.1":   ((0, 4, 1), None),
        "0.5a1":   ((0, 5, 0), ("a", 1)),
        "0.5b3":   ((0, 5, 0), ("b", 3)),
        "0.5":     ((0, 5, 0), None),
        "0.9.6":   ((0, 9, 6), None),
        "1.0":     ((1, 0, 0), None),
        "1.0.4a3": ((1, 0, 4), ("a", 3)),
        "1.0.4b1": ((1, 0, 4), ("b", 1)),
        "1.0.4":   ((1, 0, 4), None),
        "1.2.3":   ((1, 2, 3), None),
        "1.0a0":   ((1, 0, 0), ("a", 0)),
        "10.20.30b10": ((10, 20, 30), ("b", 10)),
    }


# Generated at 2026-10-25 01:36:17.484715
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():cases = [
        ("1.2", "1.2"),
        ("1.2.0", "1.2"),
        ("1.2.3", "1.2.3"),
        ("1.2a1", "1.2a1"),
        ("1.2.0b2", "1.2b2"),
        ("1.2.3a4", "1.2.3a4"),
        ("01.02.003b04", "1.2.3b4"),
    ]


# Generated at 2026-10-25 01:36:33.934502
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    class ConcreteVersion(Version):
        """Minimal concrete subclass; Version._cmp is abstract."""
        def __init__(self, value):
            self.value = value
            super(ConcreteVersion, self).__init__()

        def _cmp(self, other):
            if isinstance(other, ConcreteVersion):
                other = other.value
            if not isinstance(other, (int, float)):
                return NotImplemented
            if self.value > other:
                return 1
            elif self.value < other:
                return -1
            return 0

    v = ConcreteVersion(2)

    # Greater-than cases
    assert v > 1
    assert v > ConcreteVersion(1)

    # Not-greater cases
    assert not (v > 2)
    assert not (v > 3)
    assert not (v > ConcreteVersion(3))

    # NotImplemented propagation: comparing against an unsupported
    # type must return NotImplemented, not raise or return False.
    assert v.__gt__("not-a-version") is NotImplemented
    assert v.__gt__(None) is NotImplemented

    # Rich comparison delegates through Version.__gt__, so the bool
    # of the reflected comparison must be handled by the other operand
    # (Python falls back / raises TypeError as appropriate).
    try:
        v > object()
        raised = False
    except TypeError:
        raised = True
    assert raised, "comparison with unsupported type should raise TypeError"

# Generated at 2026-10-25 01:36:36.351268
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 01:36:38.766284
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 01:36:41.180332
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 01:36:43.595420
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:36:54.979309
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:37:00.149292
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:37:07.441525
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    class StubVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    for comparison_result, expected in [(-1, True), (0, False), (1, False)]:
        version = StubVersion(comparison_result)
        assert version.__lt__(other) is expected
        assert version.compared_with is other

    version = StubVersion(NotImplemented)
    assert version.__lt__(other) is NotImplemented
    assert version.compared_with is other