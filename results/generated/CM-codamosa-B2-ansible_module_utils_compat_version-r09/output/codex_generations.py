

# Generated at 2026-10-24 20:03:41.136684
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

    for result, expected in [(-1, True), (0, True), (1, False)]:
        version = StubVersion(result)
        assert Version.__le__(version, other) is expected
        assert version.compared_with is other

    version = StubVersion(NotImplemented)
    assert Version.__le__(version, other) is NotImplemented
    assert version.compared_with is other

# Generated at 2026-10-24 20:03:49.036492
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    class StubVersion(Version):
        def __init__(self, cmp_result):
            self.cmp_result = cmp_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.cmp_result

    other = object()

    for cmp_result, expected in ((-1, True), (0, False), (1, False)):
        version = StubVersion(cmp_result)
        assert version.__lt__(other) is expected
        assert version.compared_with is other

    version = StubVersion(NotImplemented)
    assert version.__lt__(other) is NotImplemented
    assert version.compared_with is other

# Generated at 2026-10-24 20:03:51.606681
# Unit test for constructor of class Version

# Generated at 2026-10-24 20:03:53.988762
# Unit test for constructor of class Version

# Generated at 2026-10-24 20:03:56.404936
# Unit test for constructor of class Version

# Generated at 2026-10-24 20:04:13.187925
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-24 20:04:14.518176
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    v = LooseVersion()
    v.parse("1.5.2b2")
    assert v.vstring == "1.5.2b2"
    assert v.version == [1, 5, 2, "b2"]

    v2 = LooseVersion()
    v2.parse("3.4.1.6")
    assert v2.vstring == "3.4.1.6"
    assert v2.version == [3, 4, 1, 6]

    v3 = LooseVersion()
    v3.parse("2g6")
    assert v3.vstring == "2g6"
    assert v3.version == [2, "g", 6]

# Generated at 2026-10-24 20:04:21.585570
# Unit test for constructor of class LooseVersion
def test_LooseVersion():
    version = LooseVersion("1.5.2b2")

    assert version.vstring == "1.5.2b2"
    assert version.version == [1, 5, 2, "b", 2]
    assert str(version) == "1.5.2b2"
    assert repr(version) == "LooseVersion ('1.5.2b2')"

# Generated at 2026-10-24 20:04:30.493353
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    # patch == 0 collapses to "major.minor"
    assert str(StrictVersion("1.2")) == "1.2"
    assert str(StrictVersion("1.2.0")) == "1.2"   # trailing .0 is dropped

    # patch != 0 keeps all three components
    assert str(StrictVersion("1.2.3")) == "1.2.3"
    assert str(StrictVersion("0.9.6")) == "0.9.6"

    # prerelease tag is appended (letter + number)
    assert str(StrictVersion("1.0.4a3")) == "1.0.4a3"
    assert str(StrictVersion("2.0b2")) == "2.0b2"        # patch 0 -> "2.0" + "b2"
    assert str(StrictVersion("1.2.0a1")) == "1.2a1"      # .0 dropped even with prerelease

    # round-trip: str output re-parses to an equal version
    for s in ("0.4", "0.4.0", "0.5a1", "1.0", "1.0.4b1", "2.7.13"):
        v = StrictVersion(s)
        assert StrictVersion(str(v)) == v

# Generated at 2026-10-24 20:04:46.467147
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:04:48.886261
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:04:51.308533
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:04:53.715472
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:04:56.312677
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:04:58.729570
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:05:01.148323
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 20:05:03.568173
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 20:05:05.985326
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 20:05:08.402332
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 20:05:10.819229
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 20:05:18.814707
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():assert str(StrictVersion("0.4")) == "0.4"

# Generated at 2026-10-24 20:05:27.427688
# Unit test for method __le__ of class Version
def test_Version___le__():
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
        (0, True),
        (1, False),
        (NotImplemented, NotImplemented),
    ):
        version = DummyVersion(comparison_result)
        assert version.__le__(other) is expected
        assert version.compared_with is other

# Generated at 2026-10-24 20:05:28.746994
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    # patch == 0 collapses to "major.minor"
    assert str(StrictVersion("1.2")) == "1.2"
    assert str(StrictVersion("1.2.0")) == "1.2"   # trailing .0 is dropped

    # patch != 0 keeps all three components
    assert str(StrictVersion("1.2.3")) == "1.2.3"
    assert str(StrictVersion("0.9.6")) == "0.9.6"

    # prerelease tag is appended (letter + number)
    assert str(StrictVersion("1.0.4a3")) == "1.0.4a3"
    assert str(StrictVersion("2.0b2")) == "2.0b2"        # patch 0 -> "2.0" + "b2"
    assert str(StrictVersion("1.2.0a1")) == "1.2a1"      # .0 dropped even with prerelease

    # round-trip: str output re-parses to an equal version
    for s in ("0.4", "0.4.0", "0.5a1", "1.0", "1.0.4b1", "2.7.13"):
        v = StrictVersion(s)
        assert StrictVersion(str(v)) == v

# Generated at 2026-10-24 20:05:52.004636
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 20:05:54.589536
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 20:05:57.005067
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 20:05:59.574381
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-24 20:06:02.110668
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-24 20:06:04.526344
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-24 20:06:06.943187
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-24 20:06:09.362759
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-24 20:06:11.783120
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-24 20:06:14.200491
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 20:06:16.615840
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 20:06:19.034538
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 20:06:21.450953
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:06:35.319644
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:06:48.835300
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:06:57.233232
# Unit test for method __le__ of class Version
def test_Version___le__():
    class TestVersion(Version):
        def _cmp(self, other):
            return other

    version = TestVersion()

    assert version.__le__(-1) is True
    assert version.__le__(0) is True
    assert version.__le__(1) is False
    assert version.__le__(NotImplemented) is NotImplemented

# Generated at 2026-10-24 20:07:04.778908
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

    for result, expected in [(-1, True), (0, False), (1, False)]:
        version = StubVersion(result)
        assert version.__lt__(other) is expected
        assert version.compared_with is other

    version = StubVersion(NotImplemented)
    assert version.__lt__(other) is NotImplemented
    assert version.compared_with is other

# Generated at 2026-10-24 20:07:07.203542
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:07:09.759253
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:07:12.179855
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:07:14.594530
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:07:17.259458
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:07:19.682553
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:07:22.103793
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 20:07:24.528178
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 20:07:26.939539
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 20:07:29.355964
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:07:31.771791
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:07:34.191586
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:07:36.608011
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 20:07:39.023578
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 20:07:41.441814
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 20:07:43.858909
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:07:46.275576
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:07:48.691585
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:07:57.751814
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:08:03.644335
# Unit test for method __le__ of class Version
def test_Version___le__():version = Version()

# Generated at 2026-10-24 20:08:26.425942
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 20:08:28.843560
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 20:08:31.262656
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 20:08:33.681701
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 20:08:36.099451
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 20:08:38.521446
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 20:08:40.938886
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:08:43.356748
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:08:45.771320
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:08:48.188593
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 20:08:50.604457
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 20:08:53.022589
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 20:08:55.441614
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 20:08:57.859392
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 20:09:00.279888
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 20:09:02.697004
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-24 20:09:05.117057
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-24 20:09:07.536833
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-24 20:09:09.951271
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:09:16.488896
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:09:21.637566
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:09:35.645398
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:09:38.269740
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:09:40.794900
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:09:43.211026
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 20:09:45.630759
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 20:09:48.046248
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 20:09:50.631376
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:09:53.048626
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:09:55.466056
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:10:10.724808
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:10:25.002342
# Unit test for method __ge__ of class Version
def test_Version___ge__():v1 = Version()
v2 = Version()

v1._cmp = lambda other: 1
v2._cmp = lambda other: -1

assert Version.__ge__(v1, v2) is True

# Generated at 2026-10-24 20:10:27.423514
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:10:29.841541
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:10:32.258273
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:10:34.675340
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:10:37.092205
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:10:39.508234
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:10:41.925074
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 20:10:44.342645
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 20:10:46.758615
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 20:10:49.174963
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:10:51.592452
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:10:54.008420
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:10:56.424619
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:10:58.841687
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:11:01.260098
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:11:23.474106
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 20:11:37.093131
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 20:11:39.513899
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 20:11:41.934788
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 20:11:44.353869
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 20:11:46.769276
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 20:11:49.185063
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:11:51.601310
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:11:54.021103
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:11:56.436545
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 20:11:58.852843
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 20:12:01.268848
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 20:12:03.687311
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:12:06.104953
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:12:08.524162
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:12:10.940069
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:12:13.356249
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:12:15.773954
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:12:18.190528
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:12:20.608244
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:12:23.026002
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 20:12:25.452075
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 20:12:27.869298
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 20:12:30.286452
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 20:12:32.703424
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:12:35.119639
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:12:37.537009
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:12:39.954796
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 20:12:42.374041
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 20:12:44.790649
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 20:12:47.206239
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:12:49.623548
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:12:52.044052
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:12:54.459310
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:12:56.877740
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:12:59.290186
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:13:01.707595
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:13:04.123598
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:13:06.537697
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 20:13:09.378554
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 20:13:11.794074
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 20:13:14.210928
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 20:13:16.628406
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 20:13:19.047572
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 20:13:21.465195
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 20:13:23.885808
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 20:13:26.301459
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 20:13:28.720469
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 20:13:31.137904
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 20:13:33.561875
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 20:13:35.977089
# Unit test for method __eq__ of class Version