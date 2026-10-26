

# Generated at 2026-10-25 09:44:03.850032
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:44:06.260541
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:44:08.674812
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:44:11.091998
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:44:13.503386
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:44:15.922252
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:44:18.334859
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:44:20.781845
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:44:23.163232
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:44:25.585168
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:44:27.999461
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:44:30.413732
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:44:32.873852
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:44:35.288782
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:44:37.707397
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:44:40.124321
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:44:42.538728
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:44:44.949912
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:44:47.365103
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:44:49.782883
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:44:52.197684
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:44:54.609673
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:44:57.023834
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:44:59.442951
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:45:01.858388
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:45:04.273297
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:45:06.686385
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:45:09.100391
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:45:11.518426
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:45:13.966138
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:45:16.353756
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:45:18.764060
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:45:21.179910
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:45:23.596067
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:45:26.010387
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:45:58.508833
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:46:01.482450
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:46:04.247197
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:46:06.925596
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:46:09.340697
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:46:11.757512
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:46:14.171675
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:46:16.630262
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:46:19.023251
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:46:21.437849
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:46:23.850980
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:46:26.264353
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:46:28.677988
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:46:47.339799
# Unit test for function get_closest_vowel
def test_get_closest_vowel():assert module_0.get_closest_vowel("") == ""

# Generated at 2026-10-25 09:47:01.589252
# Unit test for function get_closest_vowel
def test_get_closest_vowel():
    # Basic: rightmost interior vowel surrounded by consonants
    assert module_0.get_closest_vowel("yogurt") == "u"
    assert module_0.get_closest_vowel("FULL") == "U"
    assert module_0.get_closest_vowel("string") == "i"
    assert module_0.get_closest_vowel("cat") == "a"
    assert module_0.get_closest_vowel("cupid") == "i"  # rightmost wins over "u"

    # Too short
    assert module_0.get_closest_vowel("") == ""
    assert module_0.get_closest_vowel("a") == ""
    assert module_0.get_closest_vowel("ab") == ""

    # No qualifying vowel
    assert module_0.get_closest_vowel("quick") == ""  # adjacent vowels
    assert module_0.get_closest_vowel("queue") == ""  # adjacent vowels
    assert module_0.get_closest_vowel("apple") == ""  # vowels only at edges
    assert module_0.get_closest_vowel("bcdfg") == ""  # no vowels

# Generated at 2026-10-25 09:47:04.008366
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:47:06.674078
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:47:09.189377
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:47:11.604564
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:47:14.023568
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:47:16.437067
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:47:19.090736
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:47:21.505037
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:47:23.920326
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:47:26.338968
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:47:28.758179
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:47:31.171110
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:47:33.586661
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:47:36.003326
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:47:38.421455
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:47:40.835991
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:47:43.249342
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:47:45.664326
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:47:48.082509
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:47:50.498426
# Unit test for function get_closest_vowel

# Generated at 2026-10-25 09:47:52.996028
# Unit test for function get_closest_vowel