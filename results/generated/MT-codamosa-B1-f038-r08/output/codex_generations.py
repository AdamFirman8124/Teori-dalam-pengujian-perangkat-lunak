

# Generated at 2026-10-24 22:18:54.482848
# Unit test for function encode_cyclic

# Generated at 2026-10-24 22:18:56.897849
# Unit test for function encode_cyclic

# Generated at 2026-10-24 22:18:59.318944
# Unit test for function encode_cyclic

# Generated at 2026-10-24 22:19:01.734745
# Unit test for function decode_cyclic

# Generated at 2026-10-24 22:19:04.153787
# Unit test for function decode_cyclic

# Generated at 2026-10-24 22:19:06.572649
# Unit test for function decode_cyclic

# Generated at 2026-10-24 22:19:08.987419
# Unit test for function encode_cyclic

# Generated at 2026-10-24 22:19:11.405798
# Unit test for function encode_cyclic

# Generated at 2026-10-24 22:19:13.822707
# Unit test for function encode_cyclic

# Generated at 2026-10-24 22:19:16.243561
# Unit test for function decode_cyclic

# Generated at 2026-10-24 22:19:18.657065
# Unit test for function decode_cyclic

# Generated at 2026-10-24 22:19:21.073607
# Unit test for function decode_cyclic

# Generated at 2026-10-24 22:19:22.465542
# Unit test for function encode_cyclic
def test_encode_cyclic():
    assert module_0.encode_cyclic("") == ""
    assert module_0.encode_cyclic("a") == "a"
    assert module_0.encode_cyclic("ab") == "ab"
    assert module_0.encode_cyclic("abc") == "bca"
    assert module_0.encode_cyclic("abcd") == "bcad"
    assert module_0.encode_cyclic("abcde") == "bcdea"
    assert module_0.encode_cyclic("abcdef") == "bcadef"
    assert module_0.encode_cyclic("abcdefg") == "bcadefg"
    # round-trip property: decode(encode(s)) == s for many random strings
    import random
    import string
    for _ in range(100):
        s = "".join(random.choice(string.ascii_lowercase)
                    for _ in range(random.randint(0, 30)))
        assert decode_cyclic(module_0.encode_cyclic(s)) == s