

# Generated at 2026-10-25 07:22:20.420118
# Unit test for function histogram

# Generated at 2026-10-25 07:22:22.843421
# Unit test for function histogram

# Generated at 2026-10-25 07:22:25.258308
# Unit test for function histogram

# Generated at 2026-10-25 07:22:27.667150
# Unit test for function histogram

# Generated at 2026-10-25 07:22:30.399512
# Unit test for function histogram

# Generated at 2026-10-25 07:22:32.815546
# Unit test for function histogram

# Generated at 2026-10-25 07:22:35.229621
# Unit test for function histogram

# Generated at 2026-10-25 07:22:37.642855
# Unit test for function histogram

# Generated at 2026-10-25 07:22:40.056723
# Unit test for function histogram

# Generated at 2026-10-25 07:22:42.575577
# Unit test for function histogram

# Generated at 2026-10-25 07:22:44.988290
# Unit test for function histogram

# Generated at 2026-10-25 07:22:47.403722
# Unit test for function histogram

# Generated at 2026-10-25 07:22:49.819713
# Unit test for function histogram

# Generated at 2026-10-25 07:22:52.232688
# Unit test for function histogram

# Generated at 2026-10-25 07:22:54.650710
# Unit test for function histogram

# Generated at 2026-10-25 07:22:57.065715
# Unit test for function histogram

# Generated at 2026-10-25 07:22:59.478487
# Unit test for function histogram

# Generated at 2026-10-25 07:23:01.898154
# Unit test for function histogram

# Generated at 2026-10-25 07:23:04.310150
# Unit test for function histogram

# Generated at 2026-10-25 07:23:06.723194
# Unit test for function histogram

# Generated at 2026-10-25 07:23:09.139216
# Unit test for function histogram

# Generated at 2026-10-25 07:23:11.556154
# Unit test for function histogram

# Generated at 2026-10-25 07:23:14.016484
# Unit test for function histogram

# Generated at 2026-10-25 07:23:16.392645
# Unit test for function histogram

# Generated at 2026-10-25 07:23:18.810294
# Unit test for function histogram

# Generated at 2026-10-25 07:23:21.226720
# Unit test for function histogram

# Generated at 2026-10-25 07:23:23.636724
# Unit test for function histogram

# Generated at 2026-10-25 07:23:26.053343
# Unit test for function histogram

# Generated at 2026-10-25 07:23:28.467926
# Unit test for function histogram

# Generated at 2026-10-25 07:23:30.882472
# Unit test for function histogram

# Generated at 2026-10-25 07:23:33.307304
# Unit test for function histogram

# Generated at 2026-10-25 07:23:35.723759
# Unit test for function histogram

# Generated at 2026-10-25 07:23:38.137084
# Unit test for function histogram

# Generated at 2026-10-25 07:23:40.551203
# Unit test for function histogram

# Generated at 2026-10-25 07:23:42.967879
# Unit test for function histogram

# Generated at 2026-10-25 07:23:45.384406
# Unit test for function histogram

# Generated at 2026-10-25 07:23:47.884198
# Unit test for function histogram

# Generated at 2026-10-25 07:23:50.298774
# Unit test for function histogram

# Generated at 2026-10-25 07:24:02.067139
# Unit test for function histogram
def test_histogram():assert module_0.histogram("a b a") == {"a": 2}

# Generated at 2026-10-25 07:24:16.507119
# Unit test for function histogram
def test_histogram():
    # single winner
    assert module_0.histogram("a b b c") == {"b": 2}
    # tie: every word with the max count is returned
    assert module_0.histogram("a b c") == {"a": 1, "b": 1, "c": 1}
    assert module_0.histogram("a a b b") == {"a": 2, "b": 2}
    # one word
    assert module_0.histogram("dog") == {"dog": 1}
    # empty / all-space input -> empty dict
    assert module_0.histogram("") == {}
    assert module_0.histogram("   ") == {}
    # repeated spaces are ignored (empty tokens skipped)
    assert module_0.histogram("a  b") == {"a": 1, "b": 1}

# Generated at 2026-10-25 07:24:19.031503
# Unit test for function histogram

# Generated at 2026-10-25 07:24:21.449613
# Unit test for function histogram

# Generated at 2026-10-25 07:24:23.866407
# Unit test for function histogram