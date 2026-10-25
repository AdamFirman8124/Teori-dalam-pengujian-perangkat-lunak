

# Generated at 2026-10-24 15:25:45.904635
# Unit test for function longest

# Generated at 2026-10-24 15:25:48.316062
# Unit test for function longest

# Generated at 2026-10-24 15:25:50.731228
# Unit test for function longest

# Generated at 2026-10-24 15:25:53.146450
# Unit test for function longest

# Generated at 2026-10-24 15:25:55.560793
# Unit test for function longest

# Generated at 2026-10-24 15:25:57.976916
# Unit test for function longest

# Generated at 2026-10-24 15:26:00.389030
# Unit test for function longest

# Generated at 2026-10-24 15:26:02.802831
# Unit test for function longest

# Generated at 2026-10-24 15:26:05.220679
# Unit test for function longest

# Generated at 2026-10-24 15:26:07.635165
# Unit test for function longest

# Generated at 2026-10-24 15:26:10.049175
# Unit test for function longest

# Generated at 2026-10-24 15:26:12.460554
# Unit test for function longest

# Generated at 2026-10-24 15:26:14.873875
# Unit test for function longest

# Generated at 2026-10-24 15:26:17.288556
# Unit test for function longest

# Generated at 2026-10-24 15:26:19.700922
# Unit test for function longest

# Generated at 2026-10-24 15:26:22.113878
# Unit test for function longest

# Generated at 2026-10-24 15:26:27.813000
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

# Generated at 2026-10-24 15:26:39.077115
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["cat", "elephant", "dog"]) == "elephant"
    assert module_0.longest(["one", "two", "six"]) == "one"  # first longest is returned
    assert module_0.longest(["", "abc", "de"]) == "abc"

# Generated at 2026-10-24 15:26:46.300731
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["cat", "elephant", "dog"]) == "elephant"
    assert module_0.longest(["one", "two", "six"]) == "one"  # first longest is returned
    assert module_0.longest(["", "a", ""]) == "a"

# Generated at 2026-10-24 15:26:48.910771
# Unit test for function longest

# Generated at 2026-10-24 15:26:51.433629
# Unit test for function longest

# Generated at 2026-10-24 15:26:53.960931
# Unit test for function longest

# Generated at 2026-10-24 15:26:56.382100
# Unit test for function longest

# Generated at 2026-10-24 15:26:58.793723
# Unit test for function longest

# Generated at 2026-10-24 15:27:01.211413
# Unit test for function longest

# Generated at 2026-10-24 15:27:03.623393
# Unit test for function longest

# Generated at 2026-10-24 15:27:06.037700
# Unit test for function longest

# Generated at 2026-10-24 15:27:08.451550
# Unit test for function longest

# Generated at 2026-10-24 15:27:10.870283
# Unit test for function longest

# Generated at 2026-10-24 15:27:13.279698
# Unit test for function longest

# Generated at 2026-10-24 15:27:15.692814
# Unit test for function longest

# Generated at 2026-10-24 15:27:18.105225
# Unit test for function longest

# Generated at 2026-10-24 15:27:20.518684
# Unit test for function longest

# Generated at 2026-10-24 15:27:22.931110
# Unit test for function longest

# Generated at 2026-10-24 15:27:25.355118
# Unit test for function longest

# Generated at 2026-10-24 15:27:27.767287
# Unit test for function longest

# Generated at 2026-10-24 15:27:30.286028
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

# Generated at 2026-10-24 15:27:35.204445
# Unit test for function longest
def test_longest():
    # Empty list -> None
    assert module_0.longest([]) is None

    # Single element
    assert module_0.longest(["a"]) == "a"

    # Multiple elements, unique longest
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"

    # Tie: first longest wins
    assert module_0.longest(["aa", "bb", "c"]) == "aa"

    # All same length -> first
    assert module_0.longest(["x", "y", "z"]) == "x"

    # Lengths not sorted
    assert module_0.longest(["abc", "de", "abcd", "a"]) == "abcd"

    # Empty strings in list
    assert module_0.longest(["", "a", ""]) == "a"

    # All empty strings -> first (empty string)
    assert module_0.longest(["", ""]) == ""

    print("All tests passed.")


test_longest()

# Generated at 2026-10-24 15:27:43.077317
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["cat", "elephant", "dog"]) == "elephant"
    assert module_0.longest(["one", "two", "six"]) == "one"  # first longest string wins
    assert module_0.longest(["", "hello"]) == "hello"

# Generated at 2026-10-24 15:27:50.450444
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["cat", "elephant", "dog"]) == "elephant"
    assert module_0.longest(["one", "two", "six"]) == "one"  # first longest is returned
    assert module_0.longest(["", "a", ""]) == "a"

# Generated at 2026-10-24 15:27:52.868077
# Unit test for function longest

# Generated at 2026-10-24 15:27:55.432703
# Unit test for function longest

# Generated at 2026-10-24 15:27:57.844919
# Unit test for function longest

# Generated at 2026-10-24 15:28:00.254829
# Unit test for function longest

# Generated at 2026-10-24 15:28:02.786989
# Unit test for function longest

# Generated at 2026-10-24 15:28:05.200912
# Unit test for function longest

# Generated at 2026-10-24 15:28:07.613675
# Unit test for function longest

# Generated at 2026-10-24 15:28:10.028699
# Unit test for function longest

# Generated at 2026-10-24 15:28:12.440424
# Unit test for function longest

# Generated at 2026-10-24 15:28:14.854575
# Unit test for function longest

# Generated at 2026-10-24 15:28:17.267672
# Unit test for function longest

# Generated at 2026-10-24 15:28:19.679405
# Unit test for function longest

# Generated at 2026-10-24 15:28:22.092007
# Unit test for function longest

# Generated at 2026-10-24 15:28:24.504909
# Unit test for function longest

# Generated at 2026-10-24 15:28:26.919096
# Unit test for function longest

# Generated at 2026-10-24 15:28:29.332667
# Unit test for function longest

# Generated at 2026-10-24 15:28:31.744981
# Unit test for function longest

# Generated at 2026-10-24 15:28:34.162470
# Unit test for function longest

# Generated at 2026-10-24 15:28:36.574791
# Unit test for function longest

# Generated at 2026-10-24 15:28:38.989684
# Unit test for function longest

# Generated at 2026-10-24 15:28:41.401476
# Unit test for function longest

# Generated at 2026-10-24 15:28:43.815073
# Unit test for function longest

# Generated at 2026-10-24 15:28:46.227988
# Unit test for function longest

# Generated at 2026-10-24 15:28:48.640688
# Unit test for function longest

# Generated at 2026-10-24 15:28:51.051812
# Unit test for function longest

# Generated at 2026-10-24 15:28:53.467436
# Unit test for function longest

# Generated at 2026-10-24 15:28:55.879792
# Unit test for function longest

# Generated at 2026-10-24 15:28:58.293790
# Unit test for function longest

# Generated at 2026-10-24 15:29:00.707972
# Unit test for function longest

# Generated at 2026-10-24 15:29:03.120124
# Unit test for function longest

# Generated at 2026-10-24 15:29:05.533989
# Unit test for function longest

# Generated at 2026-10-24 15:29:07.947678
# Unit test for function longest

# Generated at 2026-10-24 15:29:10.359073
# Unit test for function longest

# Generated at 2026-10-24 15:29:19.324448
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["cat", "elephant", "dog"]) == "elephant"
    assert module_0.longest(["one", "three", "two"]) == "three"

    # When multiple strings have the same maximum length,
    # the first one should be returned.
    assert module_0.longest(["first", "second", "third"]) == "second"

# Generated at 2026-10-24 15:29:26.706284
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["cat", "elephant", "dog"]) == "elephant"
    assert module_0.longest(["hello", "world"]) == "hello"  # first longest is returned
    assert module_0.longest(["", "a", ""]) == "a"

# Generated at 2026-10-24 15:29:34.184237
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["hello", "world"]) == "hello"  # first longest is returned
    assert module_0.longest(["", "a", ""]) == "a"
    assert module_0.longest(["same", "same"]) == "same"

# Generated at 2026-10-24 15:29:36.602040
# Unit test for function longest

# Generated at 2026-10-24 15:29:39.014051
# Unit test for function longest

# Generated at 2026-10-24 15:29:41.428922
# Unit test for function longest

# Generated at 2026-10-24 15:29:43.841538
# Unit test for function longest

# Generated at 2026-10-24 15:29:46.254450
# Unit test for function longest

# Generated at 2026-10-24 15:29:48.808084
# Unit test for function longest

# Generated at 2026-10-24 15:29:51.221018
# Unit test for function longest

# Generated at 2026-10-24 15:29:53.638617
# Unit test for function longest

# Generated at 2026-10-24 15:29:56.050398
# Unit test for function longest

# Generated at 2026-10-24 15:29:58.463679
# Unit test for function longest

# Generated at 2026-10-24 15:30:00.876591
# Unit test for function longest

# Generated at 2026-10-24 15:30:03.450671
# Unit test for function longest

# Generated at 2026-10-24 15:30:05.864448
# Unit test for function longest

# Generated at 2026-10-24 15:30:08.280393
# Unit test for function longest

# Generated at 2026-10-24 15:30:10.693301
# Unit test for function longest

# Generated at 2026-10-24 15:30:13.108460
# Unit test for function longest

# Generated at 2026-10-24 15:30:15.520822
# Unit test for function longest

# Generated at 2026-10-24 15:30:17.935551
# Unit test for function longest

# Generated at 2026-10-24 15:30:20.349199
# Unit test for function longest

# Generated at 2026-10-24 15:30:22.761102
# Unit test for function longest

# Generated at 2026-10-24 15:30:25.178039
# Unit test for function longest

# Generated at 2026-10-24 15:30:27.589608
# Unit test for function longest

# Generated at 2026-10-24 15:30:30.002399
# Unit test for function longest

# Generated at 2026-10-24 15:30:32.418602
# Unit test for function longest

# Generated at 2026-10-24 15:30:47.624083
# Unit test for function longest
def test_longest():assert module_0.longest([]) is None

# Generated at 2026-10-24 15:30:55.387337
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["cat", "elephant", "dog"]) == "elephant"
    assert module_0.longest(["one", "two", "six"]) == "one"  # first longest string
    assert module_0.longest(["", "a", ""]) == "a"
    assert module_0.longest(["hello", "hi", "world"]) == "hello"

# Generated at 2026-10-24 15:31:11.801522
# Unit test for function longest
def test_longest():
    # Empty list -> None
    assert module_0.longest([]) is None

    # Single element
    assert module_0.longest(["a"]) == "a"

    # Multiple elements, unique longest
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"

    # Tie: first longest wins
    assert module_0.longest(["aa", "bb", "c"]) == "aa"

    # All same length -> first
    assert module_0.longest(["x", "y", "z"]) == "x"

    # Lengths not sorted
    assert module_0.longest(["abc", "de", "abcd", "a"]) == "abcd"

    # Empty strings in list
    assert module_0.longest(["", "a", ""]) == "a"

    # All empty strings -> first (empty string)
    assert module_0.longest(["", ""]) == ""

    print("All tests passed.")


test_longest()

# Generated at 2026-10-24 15:31:14.217372
# Unit test for function longest

# Generated at 2026-10-24 15:31:16.629065
# Unit test for function longest

# Generated at 2026-10-24 15:31:19.043047
# Unit test for function longest

# Generated at 2026-10-24 15:31:21.457979
# Unit test for function longest

# Generated at 2026-10-24 15:31:23.872081
# Unit test for function longest

# Generated at 2026-10-24 15:31:26.638411
# Unit test for function longest

# Generated at 2026-10-24 15:31:29.057777
# Unit test for function longest

# Generated at 2026-10-24 15:31:31.467782
# Unit test for function longest

# Generated at 2026-10-24 15:31:33.882227
# Unit test for function longest

# Generated at 2026-10-24 15:31:36.293765
# Unit test for function longest

# Generated at 2026-10-24 15:31:38.708417
# Unit test for function longest

# Generated at 2026-10-24 15:31:41.127170
# Unit test for function longest

# Generated at 2026-10-24 15:31:43.542634
# Unit test for function longest

# Generated at 2026-10-24 15:31:45.953827
# Unit test for function longest

# Generated at 2026-10-24 15:31:48.371217
# Unit test for function longest

# Generated at 2026-10-24 15:31:50.783592
# Unit test for function longest

# Generated at 2026-10-24 15:31:53.195846
# Unit test for function longest

# Generated at 2026-10-24 15:31:55.608896
# Unit test for function longest

# Generated at 2026-10-24 15:31:58.021104
# Unit test for function longest

# Generated at 2026-10-24 15:32:00.433774
# Unit test for function longest

# Generated at 2026-10-24 15:32:02.850388
# Unit test for function longest

# Generated at 2026-10-24 15:32:05.261721
# Unit test for function longest

# Generated at 2026-10-24 15:32:07.674763
# Unit test for function longest

# Generated at 2026-10-24 15:32:10.087450
# Unit test for function longest

# Generated at 2026-10-24 15:32:12.500860
# Unit test for function longest

# Generated at 2026-10-24 15:32:14.914313
# Unit test for function longest

# Generated at 2026-10-24 15:32:17.333630
# Unit test for function longest

# Generated at 2026-10-24 15:32:19.746033
# Unit test for function longest

# Generated at 2026-10-24 15:32:22.158112
# Unit test for function longest

# Generated at 2026-10-24 15:32:24.573491
# Unit test for function longest

# Generated at 2026-10-24 15:32:26.984232
# Unit test for function longest

# Generated at 2026-10-24 15:32:29.394973
# Unit test for function longest

# Generated at 2026-10-24 15:32:31.808417
# Unit test for function longest

# Generated at 2026-10-24 15:32:34.221799
# Unit test for function longest

# Generated at 2026-10-24 15:32:36.635271
# Unit test for function longest

# Generated at 2026-10-24 15:32:39.049262
# Unit test for function longest

# Generated at 2026-10-24 15:32:41.461479
# Unit test for function longest

# Generated at 2026-10-24 15:32:43.874743
# Unit test for function longest

# Generated at 2026-10-24 15:32:46.287547
# Unit test for function longest

# Generated at 2026-10-24 15:32:48.826207
# Unit test for function longest

# Generated at 2026-10-24 15:32:51.239727
# Unit test for function longest

# Generated at 2026-10-24 15:32:53.652400
# Unit test for function longest

# Generated at 2026-10-24 15:32:56.065048
# Unit test for function longest

# Generated at 2026-10-24 15:32:58.477316
# Unit test for function longest

# Generated at 2026-10-24 15:33:00.889680
# Unit test for function longest

# Generated at 2026-10-24 15:33:03.305019
# Unit test for function longest

# Generated at 2026-10-24 15:33:05.721416
# Unit test for function longest

# Generated at 2026-10-24 15:33:08.134750
# Unit test for function longest

# Generated at 2026-10-24 15:33:10.547664
# Unit test for function longest

# Generated at 2026-10-24 15:33:12.959798
# Unit test for function longest

# Generated at 2026-10-24 15:33:15.373724
# Unit test for function longest

# Generated at 2026-10-24 15:33:17.786627
# Unit test for function longest

# Generated at 2026-10-24 15:33:20.199516
# Unit test for function longest

# Generated at 2026-10-24 15:33:22.612816
# Unit test for function longest

# Generated at 2026-10-24 15:33:25.024566
# Unit test for function longest

# Generated at 2026-10-24 15:33:27.437100
# Unit test for function longest

# Generated at 2026-10-24 15:33:29.849884
# Unit test for function longest

# Generated at 2026-10-24 15:33:32.262780
# Unit test for function longest

# Generated at 2026-10-24 15:33:44.404378
# Unit test for function longest
def test_longest():assert module_0.longest(["cat", "elephant", "dog"]) == "elephant"

# Generated at 2026-10-24 15:33:52.538173
# Unit test for function longest
def test_longest():
    # empty list -> None
    assert module_0.longest([]) is None

    # single element
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest([""]) == ""

    # normal case: one clear longest
    assert module_0.longest(["a", "ab", "abc"]) == "abc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"
    assert module_0.longest(["a", "abc", "ab"]) == "abc"

    # tie -> first longest wins
    assert module_0.longest(["a", "b", "c"]) == "a"
    assert module_0.longest(["ab", "cd", "e"]) == "ab"
    assert module_0.longest(["e", "ab", "cd"]) == "ab"

    # with empty strings
    assert module_0.longest(["", "a", ""]) == "a"
    assert module_0.longest(["", ""]) == ""

# Generated at 2026-10-24 15:34:05.030669
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["cat", "house", "sun"]) == "house"
    assert module_0.longest(["a", "abc", "de"]) == "abc"

    # When multiple strings have the same length, return the first one
    assert module_0.longest(["cat", "dog", "bird"]) == "cat"

# Generated at 2026-10-24 15:34:52.723252
# Unit test for function longest

# Generated at 2026-10-24 15:35:41.696903
# Unit test for function longest
def test_longest():assert module_0.longest([]) is None

# Generated at 2026-10-24 15:36:02.689963
# Unit test for function longest
def test_longest():
    assert module_0.longest([]) is None
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["cat", "elephant", "dog"]) == "elephant"
    assert module_0.longest(["one", "two", "six"]) == "one"  # first longest is returned
    assert module_0.longest(["", "hello", "hi"]) == "hello"