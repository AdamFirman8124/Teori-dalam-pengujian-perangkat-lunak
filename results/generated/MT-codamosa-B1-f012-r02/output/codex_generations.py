

# Generated at 2026-10-24 20:09:37.797468
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["apple"]) == "apple"
    assert module_0.longest(["a", "abcd", "abc"]) == "abcd"
    assert module_0.longest(["cat", "dog", "bird"]) == "bird"
    assert module_0.longest(["first", "other"]) == "first"  # First string wins a tie
    assert module_0.longest(["", "a", ""]) == "a"

# Generated at 2026-10-24 20:09:40.216155
# Unit test for function longest

# Generated at 2026-10-24 20:09:42.634644
# Unit test for function longest

# Generated at 2026-10-24 20:09:45.052162
# Unit test for function longest

# Generated at 2026-10-24 20:09:47.469278
# Unit test for function longest

# Generated at 2026-10-24 20:09:49.887133
# Unit test for function longest

# Generated at 2026-10-24 20:09:52.307836
# Unit test for function longest

# Generated at 2026-10-24 20:09:54.724096
# Unit test for function longest

# Generated at 2026-10-24 20:09:57.142798
# Unit test for function longest

# Generated at 2026-10-24 20:10:02.582723
# Unit test for function longest
def test_longest():
    # Empty input returns None
    assert module_0.longest([]) is None

    # Single element
    assert module_0.longest(["a"]) == "a"

    # Unique longest
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"

    # Tie: first of the longest wins
    assert module_0.longest(["aa", "bb", "c"]) == "aa"
    assert module_0.longest(["x", "yy", "zz"]) == "yy"

    # All same length: first element returned
    assert module_0.longest(["one", "two", "six"]) == "one"

    # Mixed lengths with longest in the middle
    assert module_0.longest(["ab", "abcd", "abc"]) == "abcd"

    # Longest at the end
    assert module_0.longest(["a", "b", "longest"]) == "longest"

    # Empty string vs non-empty: empty list of strings case
    assert module_0.longest(["", ""]) == ""

    # Empty and non-empty mix
    assert module_0.longest(["", "abc"]) == "abc"

# Generated at 2026-10-24 20:10:08.208774
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["hello"]) == "hello"
    assert module_0.longest(["a", "abcd", "abc"]) == "abcd"
    assert module_0.longest(["first", "other"]) == "first"  # First on equal length
    assert module_0.longest(["", "abc", ""]) == "abc"
    assert module_0.longest(["", ""]) == ""

# Generated at 2026-10-24 20:10:13.022618
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["apple"]) == "apple"
    assert module_0.longest(["a", "abcd", "abc"]) == "abcd"
    assert module_0.longest(["first", "third", "hi"]) == "first"  # First on tie
    assert module_0.longest(["", "a", ""]) == "a"
    assert module_0.longest(["", ""]) == ""


if __name__ == "__main__":
    test_longest()
    print("All tests passed.")

# Generated at 2026-10-24 20:10:17.601652
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["apple"]) == "apple"
    assert module_0.longest(["a", "abcd", "abc"]) == "abcd"
    assert module_0.longest(["first", "other"]) == "first"  # First in a tie
    assert module_0.longest(["", "a", ""]) == "a"
    assert module_0.longest(["", ""]) == ""


if __name__ == "__main__":
    test_longest()
    print("All tests passed.")

# Generated at 2026-10-24 20:10:22.247969
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["hello"]) == "hello"
    assert module_0.longest(["a", "abcd", "abc"]) == "abcd"
    assert module_0.longest(["first", "other"]) == "first"  # First on equal length.
    assert module_0.longest(["", ""]) == ""
    assert module_0.longest(["cat", "elephant", "dog"]) == "elephant"

# Generated at 2026-10-24 20:10:24.754776
# Unit test for function longest

# Generated at 2026-10-24 20:10:27.171386
# Unit test for function longest

# Generated at 2026-10-24 20:10:29.589956
# Unit test for function longest

# Generated at 2026-10-24 20:10:32.009836
# Unit test for function longest

# Generated at 2026-10-24 20:10:34.426382
# Unit test for function longest

# Generated at 2026-10-24 20:10:36.841665
# Unit test for function longest

# Generated at 2026-10-24 20:10:39.348493
# Unit test for function longest

# Generated at 2026-10-24 20:10:41.765016
# Unit test for function longest

# Generated at 2026-10-24 20:10:44.181074
# Unit test for function longest

# Generated at 2026-10-24 20:10:46.602142
# Unit test for function longest

# Generated at 2026-10-24 20:10:49.015031
# Unit test for function longest

# Generated at 2026-10-24 20:10:51.432482
# Unit test for function longest

# Generated at 2026-10-24 20:10:53.847875
# Unit test for function longest

# Generated at 2026-10-24 20:10:56.263962
# Unit test for function longest

# Generated at 2026-10-24 20:10:58.680819
# Unit test for function longest

# Generated at 2026-10-24 20:11:01.096463
# Unit test for function longest

# Generated at 2026-10-24 20:11:03.695296
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["a", "bb", "cc"]) == "bb"
    assert module_0.longest(["abc", "def", "xyz"]) == "abc"
    assert module_0.longest(["one", "two", "three", "four"]) == "three"
    assert module_0.longest(["single"]) == "single"
    assert module_0.longest(["", "a", ""]) == "a"
    assert module_0.longest(["x", "", "yy"]) == "yy"

# Generated at 2026-10-24 20:11:10.061006
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["a", "abcd", "abc"]) == "abcd"
    assert module_0.longest(["first", "other"]) == "first"  # First on equal length
    assert module_0.longest(["", "abc", ""]) == "abc"

# Generated at 2026-10-24 20:11:15.076711
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["hello"]) == "hello"
    assert module_0.longest(["a", "abcd", "abc"]) == "abcd"
    assert module_0.longest(["first", "other"]) == "first"  # First item wins a tie
    assert module_0.longest(["", ""]) == ""

# Generated at 2026-10-24 20:11:19.275437
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["a", "abc", "ab"]) == "abc"
    assert module_0.longest(["first", "other"]) == "first"  # First on equal lengths
    assert module_0.longest(["", "a", ""]) == "a"
    assert module_0.longest(["", ""]) == ""

# Generated at 2026-10-24 20:11:24.294340
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["apple"]) == "apple"
    assert module_0.longest(["a", "abcd", "abc"]) == "abcd"
    assert module_0.longest(["first", "third", "short"]) == "first"  # First on tie
    assert module_0.longest(["", "a", ""]) == "a"
    assert module_0.longest(["", ""]) == ""

# Generated at 2026-10-24 20:11:26.910634
# Unit test for function longest

# Generated at 2026-10-24 20:11:29.423380
# Unit test for function longest

# Generated at 2026-10-24 20:11:31.841391
# Unit test for function longest

# Generated at 2026-10-24 20:11:34.259413
# Unit test for function longest

# Generated at 2026-10-24 20:11:36.690120
# Unit test for function longest

# Generated at 2026-10-24 20:11:39.105010
# Unit test for function longest

# Generated at 2026-10-24 20:11:41.523319
# Unit test for function longest

# Generated at 2026-10-24 20:11:43.944168
# Unit test for function longest

# Generated at 2026-10-24 20:11:46.511076
# Unit test for function longest

# Generated at 2026-10-24 20:11:48.927754
# Unit test for function longest

# Generated at 2026-10-24 20:11:51.344646
# Unit test for function longest

# Generated at 2026-10-24 20:11:53.762260
# Unit test for function longest

# Generated at 2026-10-24 20:11:56.179333
# Unit test for function longest

# Generated at 2026-10-24 20:11:58.596006
# Unit test for function longest

# Generated at 2026-10-24 20:12:01.012104
# Unit test for function longest

# Generated at 2026-10-24 20:12:03.430890
# Unit test for function longest

# Generated at 2026-10-24 20:12:05.849489
# Unit test for function longest

# Generated at 2026-10-24 20:12:08.267207
# Unit test for function longest

# Generated at 2026-10-24 20:12:10.686020
# Unit test for function longest

# Generated at 2026-10-24 20:12:13.103614
# Unit test for function longest

# Generated at 2026-10-24 20:12:15.521746
# Unit test for function longest

# Generated at 2026-10-24 20:12:17.939037
# Unit test for function longest

# Generated at 2026-10-24 20:12:20.356635
# Unit test for function longest

# Generated at 2026-10-24 20:12:22.773340
# Unit test for function longest

# Generated at 2026-10-24 20:12:25.190266
# Unit test for function longest

# Generated at 2026-10-24 20:12:27.606636
# Unit test for function longest

# Generated at 2026-10-24 20:12:30.021996
# Unit test for function longest

# Generated at 2026-10-24 20:12:32.438972
# Unit test for function longest

# Generated at 2026-10-24 20:12:34.855239
# Unit test for function longest

# Generated at 2026-10-24 20:12:37.276381
# Unit test for function longest

# Generated at 2026-10-24 20:12:39.694128
# Unit test for function longest

# Generated at 2026-10-24 20:12:42.109395
# Unit test for function longest

# Generated at 2026-10-24 20:12:44.525817
# Unit test for function longest

# Generated at 2026-10-24 20:12:46.943245
# Unit test for function longest

# Generated at 2026-10-24 20:12:49.363336
# Unit test for function longest

# Generated at 2026-10-24 20:12:51.780635
# Unit test for function longest

# Generated at 2026-10-24 20:12:54.197278
# Unit test for function longest

# Generated at 2026-10-24 20:12:56.612789
# Unit test for function longest

# Generated at 2026-10-24 20:12:59.029790
# Unit test for function longest

# Generated at 2026-10-24 20:13:01.448087
# Unit test for function longest

# Generated at 2026-10-24 20:13:03.864935
# Unit test for function longest

# Generated at 2026-10-24 20:13:06.283659
# Unit test for function longest

# Generated at 2026-10-24 20:13:08.701169
# Unit test for function longest

# Generated at 2026-10-24 20:13:11.118234
# Unit test for function longest

# Generated at 2026-10-24 20:13:13.535433
# Unit test for function longest

# Generated at 2026-10-24 20:13:15.949990
# Unit test for function longest

# Generated at 2026-10-24 20:13:18.365415
# Unit test for function longest

# Generated at 2026-10-24 20:13:20.783998
# Unit test for function longest

# Generated at 2026-10-24 20:13:23.201427
# Unit test for function longest

# Generated at 2026-10-24 20:13:25.618837
# Unit test for function longest

# Generated at 2026-10-24 20:13:28.035710
# Unit test for function longest

# Generated at 2026-10-24 20:13:30.449444
# Unit test for function longest

# Generated at 2026-10-24 20:13:32.866943
# Unit test for function longest

# Generated at 2026-10-24 20:13:35.288861
# Unit test for function longest

# Generated at 2026-10-24 20:13:37.704503
# Unit test for function longest

# Generated at 2026-10-24 20:13:40.122894
# Unit test for function longest

# Generated at 2026-10-24 20:13:42.539840
# Unit test for function longest

# Generated at 2026-10-24 20:13:44.959602
# Unit test for function longest

# Generated at 2026-10-24 20:13:47.376813
# Unit test for function longest

# Generated at 2026-10-24 20:13:49.795729
# Unit test for function longest

# Generated at 2026-10-24 20:13:52.212052
# Unit test for function longest

# Generated at 2026-10-24 20:13:54.856598
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["a", "bb", "cc"]) == "bb"
    assert module_0.longest(["abc", "def", "xyz"]) == "abc"
    assert module_0.longest(["one", "two", "three", "four"]) == "three"
    assert module_0.longest(["single"]) == "single"
    assert module_0.longest(["", "a", ""]) == "a"
    assert module_0.longest(["x", "", "yy"]) == "yy"

# Generated at 2026-10-24 20:14:00.659064
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["apple"]) == "apple"
    assert module_0.longest(["cat", "elephant", "dog"]) == "elephant"
    assert module_0.longest(["first", "other", "tiny"]) == "first"  # First on tie
    assert module_0.longest(["", "a", "ab"]) == "ab"

# Generated at 2026-10-24 20:14:05.074749
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["hello"]) == "hello"
    assert module_0.longest(["a", "abcd", "abc"]) == "abcd"
    assert module_0.longest(["first", "other"]) == "first"  # First item wins a tie
    assert module_0.longest(["", "a", ""]) == "a"
    assert module_0.longest(["", ""]) == ""

# Generated at 2026-10-24 20:14:08.810955
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["apple"]) == "apple"
    assert module_0.longest(["a", "abcd", "abc"]) == "abcd"
    assert module_0.longest(["first", "other", "short"]) == "first"  # First on tie
    assert module_0.longest(["", "ab", ""]) == "ab"
    assert module_0.longest(["", ""]) == ""

# Generated at 2026-10-24 20:14:13.459526
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["hello"]) == "hello"
    assert module_0.longest(["a", "abcd", "abc"]) == "abcd"
    assert module_0.longest(["first", "other", "tiny"]) == "first"  # First on tie
    assert module_0.longest(["", "ab", ""]) == "ab"
    assert module_0.longest(["", ""]) == ""

# Generated at 2026-10-24 20:14:17.964089
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["apple"]) == "apple"
    assert module_0.longest(["a", "abcd", "abc"]) == "abcd"
    assert module_0.longest(["first", "third"]) == "first"  # First longest on a tie
    assert module_0.longest(["", "ab", ""]) == "ab"
    assert module_0.longest(["", ""]) == ""

# Generated at 2026-10-24 20:14:23.084728
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["a", "abcd", "abc"]) == "abcd"
    assert module_0.longest(["cat", "dog", "bird"]) == "bird"
    assert module_0.longest(["cat", "dog"]) == "cat"  # First string wins a tie
    assert module_0.longest(["", ""]) == ""

# Generated at 2026-10-24 20:14:28.514019
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a", "abcd", "xy"]) == "abcd"
    assert module_0.longest(["cat", "dog", "a"]) == "cat"  # First longest on tie
    assert module_0.longest([""]) == ""
    assert module_0.longest(["only"]) == "only"

# Generated at 2026-10-24 20:14:31.484454
# Unit test for function longest

# Generated at 2026-10-24 20:14:33.903251
# Unit test for function longest

# Generated at 2026-10-24 20:14:36.326231
# Unit test for function longest

# Generated at 2026-10-24 20:14:38.749202
# Unit test for function longest

# Generated at 2026-10-24 20:14:41.167543
# Unit test for function longest

# Generated at 2026-10-24 20:14:43.597486
# Unit test for function longest

# Generated at 2026-10-24 20:14:46.015943
# Unit test for function longest

# Generated at 2026-10-24 20:14:48.435644
# Unit test for function longest

# Generated at 2026-10-24 20:14:50.852400
# Unit test for function longest

# Generated at 2026-10-24 20:14:53.274411
# Unit test for function longest

# Generated at 2026-10-24 20:14:55.693914
# Unit test for function longest

# Generated at 2026-10-24 20:14:58.114043
# Unit test for function longest

# Generated at 2026-10-24 20:15:00.531390
# Unit test for function longest

# Generated at 2026-10-24 20:15:02.946807
# Unit test for function longest

# Generated at 2026-10-24 20:15:05.364329
# Unit test for function longest

# Generated at 2026-10-24 20:15:07.780881
# Unit test for function longest

# Generated at 2026-10-24 20:15:10.196249
# Unit test for function longest

# Generated at 2026-10-24 20:15:12.612386
# Unit test for function longest

# Generated at 2026-10-24 20:15:15.027552
# Unit test for function longest

# Generated at 2026-10-24 20:15:17.444031
# Unit test for function longest

# Generated at 2026-10-24 20:15:20.003685
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["a", "bb", "cc"]) == "bb"
    assert module_0.longest(["abc", "def", "xyz"]) == "abc"
    assert module_0.longest(["one", "two", "three", "four"]) == "three"
    assert module_0.longest(["single"]) == "single"
    assert module_0.longest(["", "a", ""]) == "a"
    assert module_0.longest(["x", "", "yy"]) == "yy"

# Generated at 2026-10-24 20:15:24.729630
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["apple"]) == "apple"
    assert module_0.longest(["a", "abcd", "abc"]) == "abcd"
    assert module_0.longest(["first", "other"]) == "first"  # First string wins a tie
    assert module_0.longest(["", "abc", "de"]) == "abc"
    assert module_0.longest(["", ""]) == ""

# Generated at 2026-10-24 20:15:34.583725
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["a", "abcd", "abc"]) == "abcd"
    assert module_0.longest(["cat", "dog", "bird"]) == "bird"
    assert module_0.longest(["first", "other"]) == "first"  # First wins on a tie
    assert module_0.longest([""]) == ""

# Generated at 2026-10-24 20:15:39.883982
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["hello"]) == "hello"
    assert module_0.longest(["a", "abcd", "abc"]) == "abcd"
    assert module_0.longest(["first", "second", "third"]) == "second"  # First longest
    assert module_0.longest(["", ""]) == ""

# Generated at 2026-10-24 20:15:44.901714
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["apple"]) == "apple"
    assert module_0.longest(["cat", "elephant", "dog"]) == "elephant"
    assert module_0.longest(["apple", "grape", "pear"]) == "apple"  # First tie wins
    assert module_0.longest(["", "a", ""]) == "a"
    assert module_0.longest(["", ""]) == ""

# Generated at 2026-10-24 20:15:49.406635
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["hello"]) == "hello"
    assert module_0.longest(["a", "abcd", "abc"]) == "abcd"
    assert module_0.longest(["cat", "dog", "fox"]) == "cat"  # First on a tie
    assert module_0.longest(["", ""]) == ""

# Generated at 2026-10-24 20:15:53.121920
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["hello"]) == "hello"
    assert module_0.longest(["a", "abcd", "abc"]) == "abcd"
    assert module_0.longest(["first", "other"]) == "first"  # First on equal length
    assert module_0.longest(["", "abc", "de"]) == "abc"
    assert module_0.longest(["", ""]) == ""

# Generated at 2026-10-24 20:15:55.542580
# Unit test for function longest

# Generated at 2026-10-24 20:15:57.959099
# Unit test for function longest

# Generated at 2026-10-24 20:16:00.379224
# Unit test for function longest

# Generated at 2026-10-24 20:16:02.795255
# Unit test for function longest

# Generated at 2026-10-24 20:16:05.214461
# Unit test for function longest

# Generated at 2026-10-24 20:16:07.633236
# Unit test for function longest

# Generated at 2026-10-24 20:16:10.050753
# Unit test for function longest

# Generated at 2026-10-24 20:16:12.677328
# Unit test for function longest

# Generated at 2026-10-24 20:16:15.096839
# Unit test for function longest

# Generated at 2026-10-24 20:16:17.513616
# Unit test for function longest

# Generated at 2026-10-24 20:16:19.930473
# Unit test for function longest

# Generated at 2026-10-24 20:16:22.349652
# Unit test for function longest

# Generated at 2026-10-24 20:16:24.768763
# Unit test for function longest

# Generated at 2026-10-24 20:16:27.187174
# Unit test for function longest

# Generated at 2026-10-24 20:16:29.606576
# Unit test for function longest

# Generated at 2026-10-24 20:16:32.019572
# Unit test for function longest

# Generated at 2026-10-24 20:16:34.434523
# Unit test for function longest

# Generated at 2026-10-24 20:16:36.851428
# Unit test for function longest

# Generated at 2026-10-24 20:16:41.232187
# Unit test for function longest

# Generated at 2026-10-24 20:16:43.647610
# Unit test for function longest

# Generated at 2026-10-24 20:16:46.063997
# Unit test for function longest

# Generated at 2026-10-24 20:16:48.483297
# Unit test for function longest

# Generated at 2026-10-24 20:16:50.898005
# Unit test for function longest

# Generated at 2026-10-24 20:16:53.316319
# Unit test for function longest

# Generated at 2026-10-24 20:16:55.734442
# Unit test for function longest

# Generated at 2026-10-24 20:16:58.153955
# Unit test for function longest

# Generated at 2026-10-24 20:17:00.569236
# Unit test for function longest

# Generated at 2026-10-24 20:17:02.984654
# Unit test for function longest

# Generated at 2026-10-24 20:17:05.403160
# Unit test for function longest

# Generated at 2026-10-24 20:17:07.822062
# Unit test for function longest

# Generated at 2026-10-24 20:17:10.236137
# Unit test for function longest

# Generated at 2026-10-24 20:17:12.650546
# Unit test for function longest

# Generated at 2026-10-24 20:17:15.068455
# Unit test for function longest

# Generated at 2026-10-24 20:17:17.485225
# Unit test for function longest

# Generated at 2026-10-24 20:17:19.900627
# Unit test for function longest

# Generated at 2026-10-24 20:17:21.258175
# Unit test for function longest
def test_longest():
    # Empty input returns None
    assert module_0.longest([]) is None

    # Single element
    assert module_0.longest(["a"]) == "a"

    # Unique longest
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"

    # Tie: first of the longest wins
    assert module_0.longest(["aa", "bb", "c"]) == "aa"
    assert module_0.longest(["x", "yy", "zz"]) == "yy"

    # All same length: first element returned
    assert module_0.longest(["one", "two", "six"]) == "one"

    # Mixed lengths with longest in the middle
    assert module_0.longest(["ab", "abcd", "abc"]) == "abcd"

    # Longest at the end
    assert module_0.longest(["a", "b", "longest"]) == "longest"

    # Empty string vs non-empty: empty list of strings case
    assert module_0.longest(["", ""]) == ""

    # Empty and non-empty mix
    assert module_0.longest(["", "abc"]) == "abc"

# Generated at 2026-10-24 20:17:26.024629
# Unit test for function longest
def test_longest():
    assert module_0.longest(["a", "abcd", "abc"]) == "abcd"
    assert module_0.longest(["first", "other"]) == "first"  # First on equal lengths
    assert module_0.longest([""]) == ""
    assert module_0.longest([]) is None

# Generated at 2026-10-24 20:17:29.968047
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["apple"]) == "apple"
    assert module_0.longest(["a", "abcd", "abc"]) == "abcd"
    assert module_0.longest(["first", "other"]) == "first"  # First string wins a tie
    assert module_0.longest(["", "a", ""]) == "a"
    assert module_0.longest(["", ""]) == ""

# Generated at 2026-10-24 20:17:35.040949
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["hello"]) == "hello"
    assert module_0.longest(["a", "abcd", "abc"]) == "abcd"
    assert module_0.longest(["first", "other"]) == "first"  # First wins on a tie
    assert module_0.longest(["", "abc", "ab"]) == "abc"
    assert module_0.longest([""]) == ""

# Generated at 2026-10-24 20:17:39.548865
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["a", "abcd", "abc"]) == "abcd"
    assert module_0.longest(["first", "other"]) == "first"  # First item wins a tie
    assert module_0.longest(["", ""]) == ""

# Generated at 2026-10-24 20:17:51.663141
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["a", "abcd", "abc"]) == "abcd"
    assert module_0.longest(["first", "other", "third"]) == "first"  # First in a tie
    assert module_0.longest([""]) == ""

# Generated at 2026-10-24 20:17:55.361501
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["apple"]) == "apple"
    assert module_0.longest(["cat", "elephant", "dog"]) == "elephant"
    assert module_0.longest(["first", "other"]) == "first"  # First string wins a tie
    assert module_0.longest(["", "a", ""]) == "a"

# Generated at 2026-10-24 20:18:00.264796
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["a", "abcd", "abc"]) == "abcd"
    assert module_0.longest(["first", "other"]) == "first"  # First on equal length
    assert module_0.longest(["", "a", ""]) == "a"

# Generated at 2026-10-24 20:18:04.272421
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["apple"]) == "apple"
    assert module_0.longest(["a", "abcd", "abc"]) == "abcd"
    assert module_0.longest(["first", "other"]) == "first"  # First string wins a tie
    assert module_0.longest(["", "ab", ""]) == "ab"
    assert module_0.longest(["", ""]) == ""

# Generated at 2026-10-24 20:18:09.198169
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["hello"]) == "hello"
    assert module_0.longest(["a", "abcd", "abc"]) == "abcd"
    assert module_0.longest(["first", "other"]) == "first"  # First on equal lengths
    assert module_0.longest([""]) == ""
    assert module_0.longest(["", "abc", "de"]) == "abc"

# Generated at 2026-10-24 20:18:11.722390
# Unit test for function longest

# Generated at 2026-10-24 20:18:14.140715
# Unit test for function longest

# Generated at 2026-10-24 20:18:16.724144
# Unit test for function longest

# Generated at 2026-10-24 20:18:19.274025
# Unit test for function longest

# Generated at 2026-10-24 20:18:21.690742
# Unit test for function longest

# Generated at 2026-10-24 20:18:24.113440
# Unit test for function longest

# Generated at 2026-10-24 20:18:26.529197
# Unit test for function longest

# Generated at 2026-10-24 20:18:29.106289
# Unit test for function longest

# Generated at 2026-10-24 20:18:31.526218
# Unit test for function longest

# Generated at 2026-10-24 20:18:33.943023
# Unit test for function longest

# Generated at 2026-10-24 20:18:36.362032
# Unit test for function longest

# Generated at 2026-10-24 20:18:38.778795
# Unit test for function longest

# Generated at 2026-10-24 20:18:41.196235
# Unit test for function longest

# Generated at 2026-10-24 20:18:43.613523
# Unit test for function longest

# Generated at 2026-10-24 20:18:46.031648
# Unit test for function longest

# Generated at 2026-10-24 20:18:59.350120
# Unit test for function longest

# Generated at 2026-10-24 20:19:01.768198
# Unit test for function longest

# Generated at 2026-10-24 20:19:04.187992
# Unit test for function longest

# Generated at 2026-10-24 20:19:06.608286
# Unit test for function longest

# Generated at 2026-10-24 20:19:09.022248
# Unit test for function longest

# Generated at 2026-10-24 20:19:11.438942
# Unit test for function longest

# Generated at 2026-10-24 20:19:13.857570
# Unit test for function longest

# Generated at 2026-10-24 20:19:16.275795
# Unit test for function longest

# Generated at 2026-10-24 20:19:18.691623
# Unit test for function longest

# Generated at 2026-10-24 20:19:21.109177
# Unit test for function longest

# Generated at 2026-10-24 20:19:23.527877
# Unit test for function longest

# Generated at 2026-10-24 20:19:25.947146
# Unit test for function longest

# Generated at 2026-10-24 20:19:28.364135
# Unit test for function longest

# Generated at 2026-10-24 20:19:30.782595
# Unit test for function longest

# Generated at 2026-10-24 20:19:33.375540
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["a", "bb", "cc"]) == "bb"
    assert module_0.longest(["abc", "def", "xyz"]) == "abc"
    assert module_0.longest(["one", "two", "three", "four"]) == "three"
    assert module_0.longest(["single"]) == "single"
    assert module_0.longest(["", "a", ""]) == "a"
    assert module_0.longest(["x", "", "yy"]) == "yy"

# Generated at 2026-10-24 20:19:38.170337
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["apple"]) == "apple"
    assert module_0.longest(["a", "abcd", "abc"]) == "abcd"
    assert module_0.longest(["first", "other"]) == "first"  # First wins on a tie
    assert module_0.longest(["", "ab", ""]) == "ab"